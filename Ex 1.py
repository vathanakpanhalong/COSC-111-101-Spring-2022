def replace_last(array):
    new_array=[]
    for x,i in enumerate(array):
        n=(x+len(array)-1)%(len(array))
        new_array.append(array[n])
    array=new_array
    return (array)

x=replace_last([1, 2, 3, 4])
print (x)
