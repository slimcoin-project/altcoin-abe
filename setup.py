# from distutils.core import setup
import sys
from setuptools import setup, find_packages

# Find version. We have to do this because we can't import it in Python 3 until
# its been automatically converted in the setup process.
def find_version(filename):
    import re
    _version_re = re.compile(r'__version__ = "(.*)"')
    for line in open(filename):
        version_match = _version_re.match(line)
        if version_match:
            return version_match.group(1)

__version__ = find_version('Abe/version.py')

setup(
    name         = "Abe",
    version      = __version__,
    requires     = ['Crypto.Hash'],
    packages     = ['Abe', 'Abe.Chain'],
    package_data = {'Abe': ['htdocs/*.*', 'htdocs/css/*.*', 'htdocs/fonts/*.*', 'htdocs/images/*.*', 'htdocs/js/*.*']},
    author       = "John Tobey",
    author_email = "jtobey@john-edwin-tobey.org",
    url          = "https://github.com/bitcoin-abe/bitcoin-abe",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Database :: Front-Ends',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Office/Business :: Financial',
        'Topic :: Security :: Cryptography',
        #'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description  = "Abe: a free block chain browser for Bitcoin-based currencies.",
    long_description = """Abe reads the Bitcoin block chain from disk, loads
it into a database, indexes it, and provides a web interface to search
and navigate it.  Abe works with several Bitcoin-derived currencies,
including Namecoin and LiteCoin.

Abe draws inspiration from Bitcoin Block Explorer (BBE,
http://blockexplorer.com/) and seeks some level of compatibility with
it but uses a completely new implementation.""",
    )
