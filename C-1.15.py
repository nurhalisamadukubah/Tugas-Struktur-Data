def has_distinct_elements(data):
    x = set(data)
    if len(data) != len(x):
        return False
    else:
        return True

def has_distinct_elements_1(data):
    x=[]
    for a in data:
        if a in x:
            return False
        else:
            s.append(d)
    return True

print(has_distinct_elements([1,2,3,4,5,6,7,8]))
print(has_distinct_elements([1,2,3,4,5,6,7,8]))
