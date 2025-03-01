from setuptools import setup, find_packages, Extension

#######################################
# Prepare list of compiled extensions #
#######################################

extensions = []


#########
# Setup #
#########

setup(
    name='xpart',
    version='0.2.0',
    description='Generation of Particle Ensembles',
    url='https://github.com/xsuite/xpart',
    packages=find_packages(),
    ext_modules = extensions,
    install_requires=[
        'numpy>=1.0',
        'scipy',
        'xobjects'
        ]
    )
