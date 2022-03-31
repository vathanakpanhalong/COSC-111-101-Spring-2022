def replace_last(array):
    new_array=[]
    for x,i in enumerate(array):
        n=(x+len(array)-1)%(len(array))
        new_array.append(array[n])
    new_array
    return (new_array)

print(replace_last([1, 2, 3, 4]))

