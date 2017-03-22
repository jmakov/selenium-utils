#from distutils.core import setup
from setuptools import setup


setup(
    name = 'selenium_utils',
    packages = ['selenium_utils'], # this must be the same as the name above
    version = '0.2',
    description = 'Common utils for working with Selenium',
    author = 'Jernej Makovsek',
    author_email = 'jernej.makovsek@gmail.com',
    url = 'https://github.com/defactto/selenium-utils', # use the URL to the github repo
    download_url = 'https://github.com/defactto/selenium-utils/archive/0.1.tar.gz',
    keywords = ['testing', 'selenium', 'utils', 'webdriver'], # arbitrary keywords
    license = 'Apache 2.0',
    install_requires=['selenium'],
    classifiers = [
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache 2.0',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
    ],
)