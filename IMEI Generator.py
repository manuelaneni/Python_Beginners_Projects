"""IMEI GENERATOR"""
# for iPhone, Samsung and Google Phone, IMEI must start with '35'
# Skills:
# random module
# functions (include parameter)
# conditional statement

import random

def imei(device):
    IMEI = []
    device_35 = ["Apple", "Samsung", "Google", "Nokia"]
    for num in range(1, 16):
        num = random.randint(0, 9)
        IMEI.append(num)

    if device in device_35:
        IMEI[0] = 3
        IMEI[1] = 5
        for x in IMEI:
            print(x, end="")
    else:
        IMEI[0] = 8
        IMEI[1] = 6
        for x in IMEI:
            print(x, end="")


prompt = "what is the Brand of your phone"
prompt += "\n['Apple', 'Samsung', 'Google', 'Nokia']: "
imei(input(prompt).title())





































