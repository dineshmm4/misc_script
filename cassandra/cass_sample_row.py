import commands
import re

def str_to_list(given_str):
# getouput returns a string so split to make it array
        result_with_space = re.split('\n| ',given_str)
# remove empty lines
        result_no_space = [ x for x in result_with_space if x != "" ]
        return (result_no_space)

# describe key space

keyspace_str = commands.getoutput('/usr/bin/cqlsh --ssl -e "describe keyspaces"')

keyspr = str_to_list(keyspace_str)

for key in keyspr:
        cmd = '/usr/bin/cqlsh --ssl -e "use ' + key + ' ; describe tables"'
        tables_str = commands.getoutput(cmd)
        tables = str_to_list(tables_str)
        for table  in tables:
                cmd = '/usr/bin/cqlsh --ssl -e "use ' + key + ' ; select * from ' + table + ' limit 1 "'
                table_output_str = commands.getoutput(cmd)
                print (cmd)
                print (table_output_str)

