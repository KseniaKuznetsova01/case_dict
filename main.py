list = []
with open('azs.txt') as azs_file:
    for line in azs_file.readlines():
        list.append(line.split())
print(list)

#file_out = open('output.txt', 'w')
#file_out.close()
#with open('input.txt') as inp_file:
 #   for line in inp_file.readlines():

#file_out = open('output.txt', 'a')
#print(... , file = file_out)
#file_out.close()