from distutils.core import setup
import py2exe
from md2html import __VERSION__
setup(name='md2html',
	  version=__VERSION__,
	  author='Gary Campbell',
	  author_email='campg2003@gmail.com',
	  description='Convert Markdown to HTML',
	  requires=['markdown(>=2.6.6)'],
	  console=['md2html.py'])
