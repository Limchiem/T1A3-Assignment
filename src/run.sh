# !/bin/bash

echo "Hello to use this please make sure you have python3 https://www.python.org/downloads/ or visual studio code installed https://code.visualstudio.com/download"

python3 -m venv atm-venv
source atm-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py
deactivate