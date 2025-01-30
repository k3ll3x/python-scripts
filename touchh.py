#!/usr/bin/python3

import sys, datetime

tmplt = """/*
 * Author: Siegfried Keller
 * Date: $date
 *
 * Title: $title
 */

#include <math.h>

/*Functions Signature*/
void info();

void info(){
	
}"""

file = ''
if len(sys.argv) < 2:
	file = input("source file name: ")
else:
	file = sys.argv[1]

f = open(file + ".h", "w")
tmplt = tmplt.replace('$date', str(datetime.datetime.now())).replace('$title', file)
f.write(tmplt)
f.close()
exit()
