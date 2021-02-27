import codecs
import os

from setuptools import find_packages, setup

PACKAGE_NAME = "JSD"
VERSION = "0.1.0"
AUTHOR = "Tim 1"
AUTHOR_EMAIL = "tim1@gmail.com"
DESCRIPTION = "description"
KEYWORDS = "keywords"
LICENSE = "MIT"
URL = "https://github.com/tim-master2020/JSD"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    keywords=KEYWORDS,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["*.tx"]},
    install_requires=["textx_ls_core"],
    entry_points={
        'textx_languages': [
            'java_spring_boot_lang = JSD:java_spring_boot_lang',
          ],
        'textx_generators': [
            'java_spring_boot_gen = JSD:java_spring_boot_gen',
          ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)