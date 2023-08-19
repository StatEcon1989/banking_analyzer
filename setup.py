from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='banking_analyzer',
    version='0.0.1',
    packages=['banking_analyzer'],
    url='https://github.com/StatEcon1989/banking_analyzer',
    license=license,
    author='Steffen Köhler',
    author_email='Steffen.koehler@rub.de',
    description=readme,
    packages = find_packages
)
