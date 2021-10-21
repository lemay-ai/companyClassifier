# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name='smallCompanyType',
    version="3.0",
    packages=['smallCompanyType','smallCompanyType.models'],
    package_data={'': ['*.h5','*.pkl',]},
    include_package_data=True,
    install_requires=["keras>=2.6.0","transformers>=4.11.3","numpy>=1.13.3"],
)
