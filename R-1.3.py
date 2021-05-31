def minmax(data):
    if len(data):
        small = large = data[0]
        for item in data:
            if item<small:
                small = item 
            elif item>large:
                large = item
        return (small, large)
        
    else:
        print ('tidak ada data')
        return
    
print(minmax([3,9,12,7]))
print(minmax([20,5,4,8,10]))
print(minmax([]))
