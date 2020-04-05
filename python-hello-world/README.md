# python hello world project example

```
Sample example was carried out MAC-OS and steps followed described here can be used to setup this example
It's assumed you have the basic understanding of python, virual environment and pyenv.
For coding you can setup pydev eclipse and configure python 3.6 interpreter
```

## Requirements
```
Python version 3.6
virtual environment (comes with python 3.6)
```

## Setup python project used as dependency (python-test-lib2)
This will be used as dependency in python-hello-world

```
Setup a virtual environment with project name python-test-lib2 and copy all the files and directory inside it. Commands described here will install the required library and build the library (wheel and tar.gz)

pip3 install -r requirements.txt
python3 setup.py sdist bdist_wheel
cd dist
pip3 install python_test_lib2-0.0.3-py2.py3-none-any.whl
pip3 install python-test-lib2-0.0.3.tar.gz
```

## Setup python-hello-world example

```
You can run the example from command line or setup pydev eclipse and configure python interpreter. Pydev eclipse requires to configure the src, tests, data & docs folder into PYTHONPATH environment variable. It can be configured by right click --> properties.

Configure python repo under external libraries (next to PYTHONPATH) where libraries are installed. For ex: /Users/..../python3.6/site-packages
```
```
Open this project inside pydev eclipse or run the command from command line
cd python-hello-world
python3 src/__main__.py   (it will start tornado http server.. try http://localhost:8889  or http://localhost:8889/dashboard

To run the test case (unittest.trstsuite ==>)
python3 -m unittest   (additionally you can provide -s -p option to provide test file format and directory location)
```




