# Installation Instructions

This document includes installation instructions for Mac OS X
## Development Environment Configuration

* Install [Homebrew](http://brew.sh/#install)
* Install [Python](http://docs.python-guide.org/en/latest/starting/install/osx/)
* Install [VirtualEnv](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref)

## Code Checkout

Check out code from Github:

```
$ cd ~
$ mkdir -p ~git/scienceapps
$ cd scienceapps
$ git clone git@github.com:Arabidopsis-Information-Portal/PMR_API.git
```

Install & Activate Virtual Environment

```
$ cd ~git/scienceapps/PMR_API/services/metabolite_api
$ virtualenv venv
$ source venv/bin/activate
```

Install prerequsite packages:

```
$ pip install -r requirements.txt
```

## Deployment
## Documentation Building

1. Open your terminal
2. From the root source code directory run:

```
$ ./build_doc.sh
```
3. API documentation is generated in [API Doc Folder.](../../doc/api/metabolite/toc.html)


Optionally, you may customize the files included, the output format using API doc [configuration file.](doc.config)