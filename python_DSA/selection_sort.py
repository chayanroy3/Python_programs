def selectionsort(list):
    for i in range(len(list)):
        minind=i
        for j in range(i+1,len(list)):
            if list[minind]>list[j]:
                minind=j
        list[i],list[minind]=list[minind],list[i]
    print(list)

l=[5,6,4,2,3,1,9,8,7]
selectionsort(l)