names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:
names[1] = "Steven"
names[-1] = "Pepe"
names [0] = names[2] + names[4]

i = len(names)-1
for x in range(i, 0, -1):
    print(names[x])
print(names[0])