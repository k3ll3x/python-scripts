#!/usr/bin/python3

import sys, datetime

tmplt = """/*
 * Author: Siegfried Keller
 * Date: $date
 *
 * Title: $title
 */

#include <stdio.h>

/*Functions Signature*/
int main(int argc, char ** argv);

int main(int argc, char ** argv){
	
	return 0;
}"""

file = ''
if len(sys.argv) < 2:
	file = input("source file name: ")
else:
	file = sys.argv[1]

f = open(file + ".c", "w")
tmplt = tmplt.replace('$date', str(datetime.datetime.now())).replace('$title', file)
f.write(tmplt)
f.close()
exit()
