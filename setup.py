# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name='smallCompanyType',
    version="1.0",
    packages=['smallCompanyType','smallCompanyType.models'],
    package_data={'': ['*.h5','*.pkl',]},
    include_package_data=True,
    install_requires=["Keras>=2.1.2","sklearn","numpy>==1.13.3","h5py>=2.7.1"],
)
