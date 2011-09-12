#!/usr/bin/env python

import sys
import src.mp3 as mp3
import pprint

for path in sys.argv[1:]:
    total_len = 0
    total_time = 0.0
    try:
        for header,frame in mp3.frames(open(path, 'r')):
            print
            pprint.pprint(header)
            print len(frame)
            pprint.pprint(frame)
            print
            sys.stdout.flush()
            total_len += len(frame)
            total_time += mp3.time(header)
        print "GOODY GOODY total_len =",total_len
        print "GOODY GOODY total_time =",total_time
    except mp3.MP3Error, v:
        print '%s: %s' % (path, v.args[0])
    sys.stdout.flush()
