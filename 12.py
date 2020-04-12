a = 0
with open('azs.txt', "r+") as azs_file:
    for line in azs_file.readlines():
        a += 1
print(a)