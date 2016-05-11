Last updated 5/10/16 (for v0.1.1).

# Introduction
`html2md` is a tool I use in building the JAWS script for Audacity to convert `readme.md` to HTML.

# Installation:
To use the binary distribution for Windows, unpack `md2html.zip` in a folder on your path.  If you have Python, you can install it by running setup.py.  (Note: this uses `distutils` and `py2exe`, not `ez_setup`.)

# Usage:

`md2html [-t title] [-c] [-l toc_location] infile`

The input and output  use utf-8 encoding.  The output is written to `stdout`.  The options are:

- `-t`: text placed in the `<title>` element of the HTML page.
- `-c`: produce a table of contents.
- `-l`: specify the location of the table of contents.  It is a Python regular expression that matches the text in the source (Markdown) file where the TOC should appear.  The table of contents is placed just before the first match of this re.  The default is `"^# "`, which causes the TOC to be placed just before the first level 1 heading.  (Implies `-c`.)
- `-T`, `--toctitle`: a title that appears (in a span) just before the TOC.

# Configuration File
`md2html` looks for a file called `md2html.cfg` in the same folder as the source file.  It is an INI-style file containing a section for each source file in the folder.  It can currently contain keywords:

- `title=page title`: the title of the HTML page.
- `toctitle=TOC title`: text that is placed in a `<span>` element just before the TOC.

This mechanism allows for handling of titles in other languages without requiring inclusion of them in the build system.  The config file is processed using the Python [`ConfigParser`](https://docs.python.org/2/library/configparser.html) module.

## Example

```
[readme.md]
title=md2html README
toctitle=Contents:

[What's new.md]
title=What's New
toctitle="Contents"
```

You can also use a `DEFAULT` section:

```
[readme.md]
title=md2html README

[What's new.md]
title=What's New

[DEFAULT]
toctitle="Contents"
```

# Issues

- The config file is currently not utf-8 encoded.


# Conclusion
`md2html` is built using Python 2.7.10 on Windows 10 using the [Python Markdown](http://pythonhosted.org/Markdown) package v2.6.6.  It uses the `toc` and `fenced_code` extensions.  I have only tested it on Windows 10, but it should be platform-independent, however, there may be EOL and encoding issues.
