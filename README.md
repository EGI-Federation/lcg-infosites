# README for lcg-infosites package

Command line tool for the grid information system.

BDII documentation is available at
[gridinfo documentation site](https://gridinfo-documentation.readthedocs.io/).

## Installing from packages

### On RHEL-based systems

On RHEL-based systems, it's possible to install packages from
[EGI UMD packages](https://go.egi.eu/umd). The packages are build from this
repository, and tested to work with other components part of the Unified
Middleware Distribution.

> On CentOS 7, some dependencies are in [EPEL](https://docs.fedoraproject.org/en-US/epel/).

## Building packages

The [Makefile](Makefile) allows building source tarball and packages.

### Building an RPM

The required build dependencies are:

- rpm-build
- yum-utils

```shell
# Checkout tag to package
$ git clone https://github.com/EGI-Foundation/lcg-infosites.git
$ cd lcg-infosites
$ git checkout X.X.X
# Building in a container
$ docker run --rm -v $(pwd):/source -it quay.io/centos/centos:7
[root@8a9d60c61f42 /]# cd /source
[root@8a9d60c61f42 /]# yum install -y rpm-build yum-utils
[root@8a9d60c61f42 /]# yum-builddep -y lcg-infosites.spec
[root@8a9d60c61f42 /]# make rpm
```

The RPM will be available into the `build/RPMS` directory.

## Installing from source

This procedure is not for production deployment, please consider using packages.

Get the source by cloning this repository and do a `make install`.

## Preparing a release

- Prepare a changelog from the last version, including contributors' names
- Prepare a PR with
  - Updating version and changelog in
    - [CHANGELOG](CHANGELOG)
    - [lcg-infosites.spec](lcg-infosites.spec)
- Once the PR has been merged tag and release a new version in GitHub
  - Packages will be built using GitHub Actions and attached to the release page

## History

This work started under the EGEE project, and was hosted and maintained for a
long time by CERN. This is now hosted here on GitHub, maintained by the BDII
community with support of members of the EGI Federation.
