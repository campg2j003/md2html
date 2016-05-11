# 5/4/16 md2html-- convert Markdown to HTML-- for the Audacity JAWS Script project.
__VERSION__ = "0.2.1"
import sys
import os
import os.path
import argparse
import re
import io
import ConfigParser
import markdown
import markdown.extensions
# for py2exe
import markdown.extensions.fenced_code
from markdown.extensions.fenced_code import FencedCodeExtension
import markdown.extensions.toc
from markdown.extensions.toc import TocExtension


# Usage: page_template.format(page_title, body_text)
page_template = u'''\
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
	parser.add_argument("-V", "--version", action="version", version="%(prog)s v{}".format(__VERSION__), help="print program version and exit")
	parser.add_argument("input", help="input file name, - reads from stdin (default stdin)")
	parser.add_argument("-t", "--title", dest="title", help="page title")
	parser.add_argument("-c", "--toc", dest="toc", action="store_true", help="insert a table of contents")
	parser.add_argument("-l", "--toclocation", dest="toclocation", help="a Python regular expression that matches the text before which the TOC is to be placed.  Implies -c")
	parser.add_argument("-T", "--toctitle", dest="toctitle", help="title text shown (in a span) before the TOC, default ''")
	
	args = parser.parse_args(opts)
	cfg = ConfigParser.SafeConfigParser()
	if args.input and args.input != "-":
		#{
		f = io.open(args.input, mode="rt", encoding="utf-8")
		#}
	else:
		#{
		f = io.open(sys.stdin.fileno(), mode="rt", encoding="utf-8")
		#}
	#fout = io.open(sys.stdout.fileno(), mode="wt", encoding="utf-8")
	# I don't know why, but if I write this encoded I get an extra CR.  I would think writing in binary mode would produce UNIX-style line endings, but on my Windows machine it doesn't.
	fout = io.open(sys.stdout.fileno(), mode="wb")
	toc_title = ""
	page_title = ""
	if args.input and args.input != "-":
		#{
		cfgfile = os.path.dirname(args.input)
		#} # if input
	else:
		#{
			cfgfile = os.getcwd()
		#} # no input file
	cfgfile = os.path.join(cfgfile, "md2html.cfg")
	#print >>sys.stderr, "Reading config file {}".format(cfgfile) # debug
	with io.open(cfgfile, mode='rt', encoding='utf-8') as cfp:
		#{
		cfg.readfp(cfp)
		#} # with
	cfgsection = ""
	if args.input and args.input != "-":
		#{
		cfgsection = os.path.basename(args.input)
		#}
	if cfgsection:
		#{
		if cfg.has_section(cfgsection):
			#{
			#print >>sys.stderr, "cfg has section {}".format(cfgsection)
			try:
				#{
				toc_title = cfg.get(cfgsection, "toctitle")

				#} # try
			except ConfigParser.NoOptionError:
				#{
				pass
				#} # except
			try:
				#{
				page_title = cfg.get(cfgsection, "title")
				#} # try
			except ConfigParser.NoOptionError:
				#{
				pass
				#} # except
			#} # if has_section
		#} # if args.input
	if args.toctitle: toc_title = args.toctitle
	if args.title: page_title = args.title
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
		extensions.append(TocExtension(title=toc_title))
		#}
	html = markdown.markdown(s2, extensions=extensions)
	fout.write(page_template.format(page_title, html))
	f.close()
	fout.close()
	#} # main

if __name__ == "__main__":
	#{
	main(sys.argv[1:])
#} # if __main__
