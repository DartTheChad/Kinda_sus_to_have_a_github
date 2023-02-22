import sys
import os
import random
import string
length = random.randint(4, 10)

img_counter = 1
for i in range(40):
    img_name = "message{}.txt".format(img_counter)
    os.mkdir(img_name)
    img_counter += 1
