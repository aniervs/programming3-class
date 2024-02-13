my_list=[1,2,3,4,5,6,7,3,2,7]
duplicates=[x for x in my_list if my_list.count(x)>1]
duplicates=set(duplicates)
if duplicates != 0:
    print (duplicates)   
else:
    print("No duplicates found")

