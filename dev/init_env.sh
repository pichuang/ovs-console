#!/bin/sh
function install_openvswich {
    echo "Install openvswitch"
    aptitude update
    aptitude install -y libssl-dev debhelper autoconf make automake
    wget http://openvswitch.org/releases/openvswitch-2.3.2.tar.gz
    tar zxvf openvswitch-2.3.2.tar.gz
    cd openvswitch-2.3.2
    DEB_BUILD_OPTIONS='parallel=2 nocheck' fakeroot debian/rules binary

    cd ~/
    dpkg -i python-openvswitch*
    dpkg -i openvswitch-*
}

function install_devel_env {
    echo "Create develope enviroment"
    virtualenv env27 --python=python2.7
}

function into_devel_env {
    source dev/env27/bin/activate
}
