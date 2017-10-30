#!/usr/bin/python

import os
env = {"PATH":"/tmp/misc_script/fork", "XYZ":"BlaBla"}
args = ("test","abc")
res = os.execvpe("test.sh", args, env)
# the below line will not print, because the os.exec* function doesn't return anything to the called process
print("result",res)


