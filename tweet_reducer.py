#!/usr/bin/env python
import sys
import re

(last_key, curr_val) = (None, ' ')
for line in sys.stdin:
	line = line.strip()
	if not line:
		#print(line)
		continue
	else:
		(key, val) = line.strip().split(",",1)
		if last_key and last_key != key:
			print "%s,%s" % (last_key, curr_val)
			(last_key, curr_val) = (key, val)
		else:
			(last_key, curr_val) = (key, curr_val+':'+val)
			
if last_key:
	print "%s,%s" % (last_key, curr_val)
