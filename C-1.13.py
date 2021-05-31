mylist = [1, 2, 3, 4]
def reverse(data):
    temp = []
    n = len(data) - 1
    for i in range(n, -1, -1):
        temp.append(data[i])
    return temp
print('membalik urutan data')
print(mylist)
print(reverse(mylist))
