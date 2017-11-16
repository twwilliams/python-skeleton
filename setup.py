try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Tommy Williams',
    'url': 'URL to retrieve it',
    'download_url': 'Where to download it',
    'author_email': 'tommy@sapid.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
