def bubblesort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                 list[j],list[j+1]=list[j+1],list[j]
    print(list)

list1=[2,1,7,6,4,3,9,5,8]
bubblesort(list1)