import ez_setup
ez_setup.use_setuptools()
from setuptools import setup
from md2html import __VERSION__

setup(name='md2html',
	  author='Gary Campbell',
	  author_email='campg2003@gmail.com',
	  version=__VERSION__,
	  install_requires = ['markdown'],
	  py_modules=['md2html'],
	  entry_points = {'console_scripts': ['md2html = md2html:main']})
