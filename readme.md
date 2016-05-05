Last updated 5/4/16.

`html2md` is a tool I use in building the JAWS script for Audacity to convert `readme.md` to HTML.

# Usage:

`md2html [-t title] [-c] [-l toc_location] infile`

The output is written to `stdout`.  The options are:

- `-t`: text placed in the `<title>` element of the HTML page.
- `-c`: produce a table of contents.
- `-l`: specify the location of the table of contents.  It is a Python regular expression that matches the text in the source (Markdown) file where the TOC should appear.  The table of contents is placed just before the first match of this re.  The default is `"^# "`, which causes the TOC to be placed just before the first level 1 heading.  (Implies -c.)



This is built from the Python `markdown` package.  It uses the `toc` and `fenced_code` extensions.
