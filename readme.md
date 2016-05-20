Last updated 5/19/16 (for v1.0.0).

# Introduction
`html2md` is a tool I use in building the JAWS script for Audacity project to convert `readme.md` to HTML.  Although the Python markdown package, on which this tool is built, provides a command line interface, this tool is tailored to the needs of this particular project.  It provides the ability to add a table of contents without placing a `[TOC]` marker in the file, and the ability to place options in a configuration file.  It does not support all of the available features of the Python Markdown package, only the ones I use in the project for which it was made.

# Installation:
To use the binary distribution for Windows, place `md2html.exe` in a folder on your path.  If you have Python, you can install it by running `python setup.py install`.  (Uninstall it with `pip uninstall md2html`.)

# Usage:

`md2html [-q] [-t title] [-c] [-l toc_location] infile outfile`

The input and output use utf-8 encoding.  The options are:

- `-t`: text placed in the `<title>` element of the HTML page.
- `-c`: produce a table of contents.
- `-l`: specify the location of the table of contents.  It is a Python regular expression that matches the text in the source (Markdown) file where the TOC should appear.  The table of contents is placed just before the first match of this re.  If the string starts with "+", the "+" is removed and the TOC is place after the newline following the start of the matched text.  The default is `"^# "`, which causes the TOC to be placed just before the first level 1 heading.  If the string is only "+", the default is used and the TOC follows the matched line.  (Implies `-c`.)
- `-T`, `--toctitle`: a title that appears (in a span) just before the TOC.  Implies `-c`
- `-q`: Suppress informational messages


# Configuration File
`md2html` looks for a file called `md2html.cfg` in the same folder as the source file.  It is an INI-style file containing a section for each source file in the folder.  It can currently contain the following options:

- `title=page title`: the title of the HTML page.
- `toctitle=TOC title`: text that is placed in a `<span>` element just before the TOC.
- `toclocation=toc location`: same as the `-l` command line option.

This mechanism allows for handling of titles in other languages without requiring inclusion of them in the build system.  The config file is processed using the Python [`ConfigParser`](https://docs.python.org/2/library/configparser.html) module.  Command line options override configuration file options.

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

- The config file option values read from the command line are not utf-8 encoded.  Since they are inserted into HTML, it should be possible to use &# substitutions.
- In order to make this Python program into a stand-alone executable, it is packaged in a NSIS installer that installs the necessary files in a temp folder, runs the program, and deletes the temp folder.  When this executable is run from a .cmd file, messages do not appear in the output.  They do appear if the program is run from Python, if the executable produced by py2exe is run from a CMD file, or if the NSIS executable is run directly.


# Conclusion
`md2html` is built using Python 2.7.10 on Windows 10 using the [Python Markdown](http://pythonhosted.org/Markdown) package v2.6.6.  It uses the `toc` and `fenced_code` extensions.  I have only tested it on Windows 10, but it should be platform-independent, however, there may be EOL and encoding issues.

To build the binary executable distribution file, run:

```
python setupexe.py py2exe
makensis setup.nsi
```

The finished executable will be in your working directory.
