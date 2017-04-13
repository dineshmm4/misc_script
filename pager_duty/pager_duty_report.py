#!/usr/local/bin/python

from pandas.io.json import json_normalize 
import pdconfig as pdc
import requests
import json
import csv

def list_incidents(offset_value):
    url = 'https://api.pagerduty.com/incidents'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=pdc.api_config['API_KEY'])
    }
    payload = {
        'since': pdc.api_config['SINCE'],
        'until': pdc.api_config['UNTIL'],
        'time_zone': pdc.api_config['TIME_ZONE'],
        'limit' : pdc.api_config['LIMIT'],
        'offset' : offset_value
    }
    r = requests.get(url, headers=headers, params=payload)
    #print ('Status Code: {code}'.format(code=r.status_code))
    return (r.json())

if __name__ == '__main__':
    temp = []
    for i in range(1,pdc.api_config['LOOP'],100):
        result = list_incidents(i)
        #print("Loop => ",i,"offset => ", result['offset'])
        temp = temp + result['incidents']
        
        df = json_normalize(temp)
        df.to_csv('PagerDutyReport_csvformat.csv')
