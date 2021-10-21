# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name='smallCompanyType',
    version="3.0",
    packages=['smallCompanyType','smallCompanyType.models'],
    package_data={'': ['*.h5','*.pkl',]},
    include_package_data=True,
    install_requires=["Keras>=2.1.2","transformers","numpy>=1.13.3"],
)
