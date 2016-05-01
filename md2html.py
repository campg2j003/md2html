# 4/27/16 md2html-- convert Markdown to HTML-- for the Audacity JAWS Script project.

import sys
import os
import os.path
import argparse
import markdown
import markdown.extensions

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
	parser.add_argument("-t", dest="title", help="page title")
	
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
	html = markdown.markdown(s, extensions=['markdown.extensions.toc', 'markdown.extensions.fenced_code'])
	fout.write(page_template.format(args.title, html))
	#} # main

if __name__ == "__main__":
	#{
	main(sys.argv[1:])
#} # if __main__
