# README for lcg-infosites package

Command line tool for the grid information system.

## Installing from source

```sh
make install
```

## Building packages

### Building a RPM

The required build dependencies are:

- rpm-build
- make

```sh
# Checkout tag to be packaged
git clone https://github.com/EGI-Foundation/lcg-infosites.git
cd lcg-infosites
git checkout X.X.X
# Building in a container
docker run --rm -v $(pwd):/source -it centos:7
yum install -y rpm-build make rsync
cd /source && make rpm
```

The RPM will be available into the `build/RPMS` directory.

### Building a deb

```sh
# Checkout tag to be packaged
git clone https://github.com/EGI-Foundation/lcg-infosites.git
cd lcg-infosites
git checkout X.X.X
# Building in a container using the source files
docker run --rm -v $(pwd):/source -it ubuntu:xenial
apt update
apt install -y devscripts debhelper make python-all-dev
cd /source && make deb
```

The DEB will be available into the `build/` directory.

## History

This work started under the EGEE project, and was hosted and maintained for a
long time by CERN.
This is now hosted here on GitHub, maintained by the BDII community with
support of members of the EGI Federation.
