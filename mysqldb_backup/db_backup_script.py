#!/usr/local/bin/python

from __future__ import print_function
import os
import time
import datetime
import subprocess
import db_backup_config as dbc 
import smtplib
from email.mime.text import MIMEText


# Send mail on error

def send_mail(body):
	msg=MIMEText(body)
	msg['Subject'] = 'Mysql dump/backup Failed, please check'
	msg['From'] = dbc.db_config['EMAIL_FROM'] 
	msg['To'] = dbc.db_config['EMAIL_TO'] 
	
	s = smtplib.SMTP('localhost')
	s.sendmail(dbc.db_config['EMAIL_FROM'], [dbc.db_config['EMAIL_TO']], msg.as_string())
	s.quit()


# Reading configs

DB_HOST = dbc.db_config['HOSTNAME']
DB_USER = dbc.db_config['USER'] 
DB_USER_PASSWD = dbc.db_config['DB_USER_PASSWD'] 
DB_NAME = dbc.db_config['DB_NAME'] 
BACKUP_PATH = dbc.db_config['BACKUP_PATH'] 


# Check if DB path exists, if not create one 

if not os.path.exists(BACKUP_PATH):
	os.makedirs(BACKUP_PATH,755)


# Construct backup command

TIMESTAMP = datetime.datetime.today().strftime('%Y-%m-%d-%H-%M')
DB_BACKUP_NAME = DB_NAME + "_" + TIMESTAMP + ".sql" 

dumpcmd = "/usr/bin/mysqldump -u" + DB_USER + " -p" + DB_USER_PASSWD + " --single-transaction --routines --triggers --databases " + DB_NAME + " > " + BACKUP_PATH + DB_BACKUP_NAME 


# Excute backup command 
# Shell = True to send command as string instead of list

print ("Mysql dump is running for " + DB_NAME + "\n" + "File is at ",BACKUP_PATH + DB_BACKUP_NAME)
sp = subprocess.Popen(dumpcmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
out, err = sp.communicate()

body = "Mysql DB Backup failed for  " + DB_NAME + "\n" 
body += err

if (sp.returncode > 0 ):
	send_mail(body)
else:
	gzipcmd = "/usr/bin/gzip -c < " + BACKUP_PATH + DB_BACKUP_NAME + " > " + BACKUP_PATH +  DB_BACKUP_NAME + ".gz"
	print("Gzip is running for File ",BACKUP_PATH,DB_BACKUP_NAME)
	print(gzipcmd)
	sp = subprocess.Popen(gzipcmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
	out, err = sp.communicate()
	body += " gzip command failed " + gzipcmd

	if (sp.returncode > 0 ):
		send_mail(body)
