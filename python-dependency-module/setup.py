
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='python-test-lib2',  
    version="0.0.3",
    description='A sample Python project', 
    long_description=long_description,  
    long_description_content_type='text/markdown', 
    url='https://github.com/pypa/sampleproject', 
    author='Pankaj Singh',
    author_email='xxxx@gmail.com',  
    classifiers=[ 
        'Development Status :: 3 - Alpha', 
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
    ],
 
    keywords='sample setuptools development',  
    package_dir={'': 'src'},  
    packages=find_packages(where='src'),
    python_requires='>=3.6', 
    entry_points={  # Optional
        'console_scripts': [
            'python-test-lib2=__main__:main',
        ],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/pypa/sampleproject/',
    },
)
