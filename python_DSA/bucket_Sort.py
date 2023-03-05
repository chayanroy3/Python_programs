from insertion_sort import insertionsort
import math as m
def bucketsort(list):
    nbucket=round(m.sqrt(len(list)))
    maxval=max(list)
    arr=[]
    for i in range(nbucket):
        arr.append([])
    for j in list:
        index_b=m.ceil(j*nbucket/maxval)
        arr[index_b-1].append(j)
    for i in range(nbucket):
        arr[i]=insertionsort(arr[i])
    
    #marging the buckets
    k=0
    for i in range(nbucket):
        for j in range(len(arr[i])):
            list[k]=arr[i][j]
            k+=1
    return list
l= [1,9,3,5,7,6,4,2,8]
print(bucketsort(l))