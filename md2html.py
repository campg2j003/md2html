# 5/4/16 md2html-- convert Markdown to HTML-- for the Audacity JAWS Script project.

import sys
import os
import os.path
import argparse
import re
import markdown
import markdown.extensions
# for py2exe
import markdown.extensions.fenced_code
from markdown.extensions.fenced_code import FencedCodeExtension
import markdown.extensions.toc
from markdown.extensions.toc import TocExtension


# Usage: page_template.format(page_title, body_text)
page_template = '''\
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>{}</title>
</head>
<body>
{}
</body>
</html>
'''

desc = """\
Convert Markdown to HTML.  Writes to stdout"""

def main(opts):
	#{
	"""@param opts: list of command line args-- sys.argv[1:].
	@type opts: list of string"""
	parser = argparse.ArgumentParser(description=desc, argument_default="", fromfile_prefix_chars="@")
	parser.add_argument("input", help="input file name, - reads from stdin (default stdin)")
	parser.add_argument("-t", "--title", dest="title", help="page title")
	parser.add_argument("-c", "--toc", dest="toc", action="store_true", help="insert a table of contents")
	parser.add_argument("-l", "--toclocation", dest="toclocation", help="a Python regular expression that matches the text before which the TOC is to be placed.  Implies -c")
	parser.add_argument("-T", "--toctitle", dest="toctitle", help="title text shown (in a span) before the TOC, default ''")
	
	args = parser.parse_args(opts)
	if args.input and args.input != "-":
		#{
		f = open(args.input)
		#}
	else:
		#{
		f = sys.stdin
		#}
	fout = sys.stdout
	s = f.read()

	toc = args.toc
	toclocation = args.toclocation
	if toclocation: toc = True
	if toc:
		#{
		if not toclocation: toclocation = "^# "
		s2 = re.sub(toclocation, R"[TOC]\n\g<0>", s, 1, re.M)
		#} # if toc
	else:
		#{
		s2 = s
		#} # else not toc
	#print s2 # debug
	#print "-- after s2" # debug
	extensions = [FencedCodeExtension()]
	if toc:
		#{
		toc_title = args.toctitle
		extensions.append(TocExtension(title=toc_title))
		#}
	html = markdown.markdown(s2, extensions=extensions)
	fout.write(page_template.format(args.title, html))
	#} # main

if __name__ == "__main__":
	#{
	main(sys.argv[1:])
#} # if __main__
