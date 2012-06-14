#!/bin/bash

PIP_LOC=`which pip`

echo "Checking for pip..."
if [ -z "${PIP_LOC}" ]; then
    echo "Not found, installing pip"
    sudo easy_install pip
fi

echo "Checking for virtualenv..."
VE_LOC=`which virtualenv`
if [ -z "${VE_LOC}" ]; then
    echo "Not found, installing virtualenv"
    sudo pip install virtualenv
fi

echo "Setting up virtualenv for the first time."
virtualenv ve

echo "Activating..."
source ve/bin/activate

echo "Installing integration_tools site-package dependencies"
pip install restkit


# TODO: Figure out how to permanently append git-* tools to the user's path.