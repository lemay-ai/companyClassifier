# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name='companyClassifier',
    version="3.0.0",
    packages=['companyClassifier','companyClassifier.models'],
    package_data={'': ['*.json','*.joblib','*.h5']},
    include_package_data=True,
    install_requires=["wget","keras>=2.6.0","tqdm","joblib","transformers>=4.11.3","numpy>=1.13.3","tensorflow>=2.6.0"],
)
