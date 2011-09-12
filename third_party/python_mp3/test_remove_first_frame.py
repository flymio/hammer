#!/usr/bin/env python

import sys
import src.mp3 as mp3
import pprint

srcFile = sys.argv[1]
dstFile = sys.argv[2]

fpOut = open(dstFile,'wb')

total_len = 0
total_time = 0.0
firstFrame = True
try:
    for header,frame in mp3.frames(open(srcFile, 'r')):
        print
        pprint.pprint(header)
        print len(frame)
        pprint.pprint(frame)
        print
        sys.stdout.flush()
        total_len += len(frame)
        total_time += mp3.time(header)
        if firstFrame:
            firstFrame = False
        else:
            fpOut.write(frame)
    print "GOODY GOODY total_len =",total_len
    print "GOODY GOODY total_time =",total_time
except mp3.MP3Error, v:
    print "error ",str(v)
    #print '%s: %s' % (path, v.args[0])
sys.stdout.flush()

fpOut.close()
