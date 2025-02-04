list1 = [3, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = ['giorgi', 'nika', 'saba', 'sandro', 'luka', 'saba', 'daviti', 'mate', 'mariami', 'nino']
list3 = [10, 2000, 300, 444, 500, 600, 777, 800, 900, 100000]
list4 = [True, False, True, False, True, False, True, False, True, False]

print( list1[:4])

print()
for i in range(3, 8):  
    print(list2[i])

print( list3[8:5:-1])

print()
index = 0
while index < len(list4):
    print(list4[index])
    index += 1
