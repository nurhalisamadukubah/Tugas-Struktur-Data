def jumlah_ganjil_squares(n):
    sum = 0
    for nomor in range(n):
        if nomor%2 == 0:
            continue
        sum += nomor**2
    return sum
print('penjumlahan untuk nilai ganjil kurang dari n')
print(jumlah_ganjil_squares(6))
