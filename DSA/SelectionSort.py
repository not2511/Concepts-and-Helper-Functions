def selection_sort(list):
    for i in range(len(list)-1):
        min_index=i
        for j in range(i+1,len(list)-1):    #len(list)-1 or len(list) 
            if list[j]<list[min_index]:
                min_index=j
        if i!=min_index:
            temp=list[i]
            list[i]=list[min_index]
            list[min_index]=temp
    return list

print(selection_sort([1,5,87,23,98,33,2,78,890]))