def sum_squares(n):
    sum = 0
    for nomor in range(0,n):
        sum+=nomor**2
    return sum
print('sum of the squares')
print(sum_squares(4)) 
