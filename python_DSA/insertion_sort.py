def insertionsort(list):
    for i in range(1,len(list)):
        key=list[i]  #which is to be sifted to sorted part
        j=i-1
        while j>=0 and key < list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]= key
    return list

