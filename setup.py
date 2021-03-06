from setuptools import setup, find_packages
import re
import os


long_description = (
    'Python library which implements Succesive Halving and Classification '
    'for Parallel Architecture and Hyper Parameter Search from the paper '
    '[Parallel Architecture and Hyperparameter Search via Successive Halving '
    'and Classification](https://arxiv.org/abs/1805.10255).'
)


def get_version(package):
    """Return package version as listed in `__version__` in `init.py`."""
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name='pyshac',
    version=get_version("pyshac"),
    packages=find_packages(),
    url='https://github.com/titu1994/pyshac',
    download_url='https://github.com/titu1994/pyshac',
    license='MIT',
    author='Somshubra Majumdar',
    author_email='titu1994@gmail.com',
    description='Python library which implements Succesive Halving and Classification algorithm',
    long_description=long_description,
    install_requires=['numpy>=1.14.2',
                      'scikit-learn>=0.19.1',
                      'pandas>=0.19.2',
                      'joblib>=0.12',
                      'loky>=2.1.4',
                      'cloudpickle>=0.5.3',
                      'six>=1.11.0',
                      'xgboost>=0.72'],
    classifiers=(
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
    zip_safe=False,
    test_suite="tests",
)
