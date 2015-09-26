#!/usr/bin/env python
import sys, hashlib, urllib2

def spacejam256(data):
    #Everybody get up it's time to slam now
    req = urllib2.Request('http://www.warnerbros.com/archive/spacejam/movie/jam.htm')
    
    #We got a real jam goin' down
    salt = urllib2.urlopen(req).read()
    
    #Welcome to the Space Jam
    h = hashlib.sha256()
    
    #Here's your chance do your dance at the Space Jam
    h.update(data + salt)

    #Alright
    return h.hexdigest()

print spacejam256(sys.argv[1])
