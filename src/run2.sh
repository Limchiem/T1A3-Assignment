# !/bin/bash

echo "Hello please wait a moment for packages to finish installing."

python3 -m venv atm-venv
source atm-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py
deactivate