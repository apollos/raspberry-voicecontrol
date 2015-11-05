try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description': 'A basic deamon run on raspberry Pi to recognize voice control and give relative response or answer or action',
    'author': 'Song Yu',
    'url': 'https://github.com/apollos/raspberry-voicecontrol',
    'author_email': 'apollos521@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['rock1'],
    'scripts': [],
    'name': 'raspberry-voicecontrol'
]

setup(**config)
