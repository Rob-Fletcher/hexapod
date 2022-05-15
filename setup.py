from setuptools import setup
from hexapod import __version__


setup(
    name='hexapod',
    version=__version__,
    packages=['hexapod'],
    install_requires=[
        'adafruit_circuitpython_servokit'
    ]
)