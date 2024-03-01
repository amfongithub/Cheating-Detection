#! /bin/sh
# shellcheck disable=SC1046
# shellcheck disable=SC1073
if command -v python3 &>/dev/null; then
    echo "Python 3 is installed"
else
    echo "Python 3 is not installed NOW installing python3"
    # shellcheck disable=SC1047
    # shellcheck disable=SC1072
    # shellcheck disable=SC1072
    && sudo apt-get update \
    && sudo apt-get upgrade python3
if	\
sudo apt install python3-pip \
&& sudo apt install --upgrade python3-pip \
&& pip3 install matplotlib \
&& pip3 install numpy \
&& pip3 install opencv-python
