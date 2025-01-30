#!/usr/bin/python3

import sys, os, re

def usage():
	print("{0} cppfilename".format(sys.argv[0]))

if len(sys.argv) < 2:
	usage()
	sys.exit(1)

_filename = sys.argv[1]
filename = _filename
module = "myModule"

f = open(sys.argv[1], encoding='utf-8', errors='ignore')
txt = f.read()
f.close()

txt = re.sub("//.*\n","",txt)
txt = re.sub(",\n",",",txt)

filename = "tmp.{0}".format(sys.argv[1])
f = open(filename,"w")
f.write(txt)
f.close()

cmd = 'ctags -x --_xformat="%K#%N#%C" {0} | grep function'.format(filename)

txt = os.popen(cmd).read()

l = re.findall("function#.*#.*[(].*[)]",txt)

txt = """#include "{0}"
#include <emscripten/bind.h>

using namespace emscripten;

EMSCRIPTEN_BINDINGS({1}""".format(_filename, module) + "){\n"

for i in l:
	try:
		nl = i.split('#')
		txt += '\tfunction("{0}",&{0});\n'.format(nl[1])
	except:
		pass

txt += "}\n"

filename = filename.replace("tmp.","")
# filename = "_" + re.findall("\w+",filename)[0] + ".cc"
filename = "main.cc"
f = open(filename, "w")
f.write(txt)
f.close()

os.popen("cat {0} | uniq > tmpf && mv tmpf {0}".format(filename)).read()
os.popen("rm tmp*")
