from setuptools import setup
setup(name='assgnopts',
      version='1.0',
      description='A plugin to ask the user',
      url='https://github.com/acalasanzs/assgnopts',
      author='Albert Calasanz',
      author_email='acsestudios02@gmail.com',
      license='MIT',
      packages=['assgn',"opts"],
      zip_safe=False)
from distutils.core import setup
setup(
  name = 'assgnopts',         # How you named your package folder (MyLib)
  packages = ['assgnopts'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = "It's a console input improvement, and and options in class digger",   # Give a short description about your library
  author = 'Albert Calasanz',                   # Type in your name
  author_email = 'acsstudiosdev@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/acsstudios/assgnopts',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/acsstudios/assgnopts/archive/refs/tags/Assgn1.0.tar.gz',    # I explain this later on
  keywords = ['assgn', 'input', 'optionsinclass'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)