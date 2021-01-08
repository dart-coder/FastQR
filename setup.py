from subprocess import call
from os import remove
from json import dump, load

call("setup.sh", shell=True)

with open("token.txt", encoding="utf-8") as file:
    TOKEN = file.read()

remove("token.txt")

with open("config.json", encoding="utf-8") as file:
    CONFIG_DICT = load(file)

CONFIG_DICT["TOKEN"] = TOKEN

with open("config.json", encoding="utf-8", mode="w") as file:
    dump(CONFIG_DICT, file, indent=4)