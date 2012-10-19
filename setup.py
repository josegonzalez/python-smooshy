from distutils.core import setup

setup(
    name='smooshy',
    version='1',
    author='Jose Gonzalez',
    author_email='support@savant.be',
    packages=['smooshy'],
    scripts=['bin/smooshy'],
    url='https://github.com/josegonzalez/smooshy',
    license='LICENSE.txt',
    description='Automatic lossless image compression',
    long_description=open('README.rst').read(),
    install_requires=['simplejson']
)
