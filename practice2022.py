base_str = input()

list_1 = []
for char in base_str:
    n = ord(char) - 97
    list_1.append(n)

list_2 = []
temp = list_1[0]

if (temp > 5):
    list_2.append(temp - 5)
else:
    list_2.append(temp - 5 + 26)
    
for n in list_1[1:]:
    while (n < temp):
        n = n + 26
    list_2.append(n - temp)
    temp = n
   
for i in range(len(list_2)):
    list_2[i] = chr(list_2[i] + 97)

print ("".join(list_2))
