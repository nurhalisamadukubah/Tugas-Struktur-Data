def penjumlahan_ganjil_squares1(n):
    return sum(b*b for b in range(0,n) if b%2!=0)

print('penjumlahan untuk nilai ganjil kurang dari n part 2')
print(penjumlahan_ganjil_squares1(6))
