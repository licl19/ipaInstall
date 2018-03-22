#!/usr/bin/python
# -*- coding: UTF-8 -*-

# chmod +x transporter_chief.rb

from Tkinter import * 
from tkMessageBox import *
import urllib
import urllib2
import time
import json
import os, sys, string, socket
from array import *

reload(sys)
sys.setdefaultencoding('utf-8')

def downloadapp():
# ipaName,url 根据具体情况写入
    ipaName = ''
    url = ''
    fipa = urllib2.urlopen(url)
    dataipa = fipa.read()
    fipawrite = open(ipaName, "wb")
    fipawrite.write(dataipa)
    fipawrite.close()
    installapp(ipaName)
    pass

def installapp(ipaName):
    print(os.getcwd())
    command = "./transporter_chief.rb" + " " + ipaName
    os.system(command) #安装ipa
    os._exit(0)
    pass

if __name__ == "__main__":
    downloadapp()


