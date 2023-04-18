from random import choice
from datetime import datetime

def slugify():
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowers = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    date = str(datetime.now()).replace(" ", "")
    date = date.replace(":", "")
    date = date.replace(".", "")
    date = date.replace("-", "")
    slug = ""
    for i in range(5):
        slug += choice(uppers)
        slug += choice(lowers)
        slug += choice(digits)
        slug += choice(date) 
    return slug

with open("test.txt", "w") as f:
    for i in range(10000):
        a = slugify()
        f.write(a)
        f.write("\n")
print(a)