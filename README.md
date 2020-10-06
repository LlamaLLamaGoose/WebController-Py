## WebController-Py

I quickly threw this together using [Onkyo-eiscp](https://github.com/miracle2k/onkyo-eiscp).

I created this so co-workers can control the volume of spotify while they take calls etc

## Todo
* Update the UI to be better.
* Take some variables into something like an .env file
* try to add spotify api so you can skip songs etc


## Installation
```
apt-get install python3-devel
apt-get install gcc-core
apt-get install libcrypt-devel

You might need to do this if you don't have access to pip for python3
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

python3 -m pip install flask
python3 -m easy_install onkyo-eiscp

cd into WebController-Py-master
python3 -m webcontroller.py
```
