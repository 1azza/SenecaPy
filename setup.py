from setuptools import setup, find_packages
import codecs
import os



VERSION = '1.0.0b1'
DESCRIPTION = 'senecalearning.com API wrapper'

# Setting up
setup(
    name="SenecaPy",
    version=VERSION,
    author="1azza (Larry Rennoldson)",
    author_email="rennoldsonlarry@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'cheat', 'seneca', 'API', 'wrapper', 'requests'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)