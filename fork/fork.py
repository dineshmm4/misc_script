#!/usr/bin/python

"""
# https://www.python-course.eu/forking.php

in the parent copy the os.fork() will return a postive value 
in the child copy the os.fork() will return a 0 value

using newpid 0 or positive value we distinguish between the the child and the parent job

"""

import os

def child():
   print('\nA new child ',  os.getpid())
   os._exit(0)  

def parent():
   while True:
      newpid = os.fork()
      if newpid == 0:
         child()
      else:
         pids = (os.getpid(), newpid)
         print("parent: %d, child: %d\n" % pids)
      reply = input("2 for quit / 1 for new fork")
      if reply == 1: 
          continue
      else:
          break

parent()
