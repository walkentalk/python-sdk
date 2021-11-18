import json
import urllib.request
import sys
import blocknative
from distutils.version import StrictVersion

def pypi_url(package:str):
    PYPI_URL = 'https://pypi.org/pypi/%s/json'
    return PYPI_URL % package

def latest_version(package:str):
    url = pypi_url(package)
    with urllib.request.urlopen(url) as packagestream:
        package = json.load(packagestream)
        releases = package['releases'].keys()
        releases = list(releases)
        releases.sort(key = StrictVersion, reverse=True)
        last = releases[0]
        releases.append(blocknative.__version__)
        releases.sort(key = StrictVersion, reverse=True)
        current = releases[0]
        if current != blocknative.__version__ and last != releases[1]:
            print('Current version is %s, attempt to update to %s' % (last, current))
            sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for package in sys.argv[1:]:
            latest_version(package)
    else:
        print('%s packagename' % sys.argv[0])
        sys.exit(1)
