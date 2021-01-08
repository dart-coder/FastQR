#!bin/bash

python -m pip install --upgrade pip
pip install -r requirements.txt
echo -n "Enter your Telegram Bot Token: "
read token
echo -n $token > token.txt