from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Developers',
  'License :: OSI Approved :: MIT License',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'Programming Language :: Python :: 3.12'
]
 
setup(
  name='netpro',
  version='0.1.0',
  description='A Python library for basic network protocols',
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  url='https://github.com/TareqAbeda/netpro',  
  author='Tareq Abeda',
  author_email='TareqAbeda0@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='netpro', 
  packages=find_packages(),
  install_requires=[] 
)