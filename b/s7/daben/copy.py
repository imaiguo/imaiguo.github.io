#!/usr/bin/python
#test_copyfile.py

import os,shutil

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!"%(srcfile)
    else:
        fpath,fname=os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.copyfile(srcfile,dstfile)
        print "copy %s -> %s"%( srcfile,dstfile)

srcfile='./001.html'
dstfile='./002.html'

count = 1
while (count < 800):
	count = count + 1
	if(count < 10):
		file = "./00"+str(count) + ".html"
	elif(count < 100):
		file = "./0"+str(count) + ".html"
	else:
		file = "./"+str(count) + ".html"
	mycopyfile(srcfile,file)