def insertion_sort(list):
    for i in range(1,len(list)):
        temp=list[i]
        j=i-1
        while temp<list[j] and j>-1:
            list[j+1]=list[j]
            list[j]=temp
            j-=1 
    return list

print(insertion_sort([4,1,7,5,2,3,10]))