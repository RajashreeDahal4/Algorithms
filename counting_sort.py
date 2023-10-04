'''
Date: October 3, 2023
Name: Rajashree Dahal
Problem Statement:
Apply counting sort to sort the following array: [2,3,0,1,2,2,3,0,1,2].
Show the counting array C after counting and finishing placing each number in the sorted array. 
'''
def counting_sort(array_list):
    min_element=min(array_list)
    max_element=max(array_list)
    counting_array=[]
    for i in range(min_element,max_element+1):
        counting_array.append(array_list.count(i))

    sorted_array=[]
    for enum,i in enumerate(counting_array):
        if i==0:
            continue
        else:
            sorted_array.extend([enum]*i)

    print("The counting array is",counting_array)
    print("The sorted array using counting sort is",sorted_array)
        
array_list=[2,3,0,1,2,2,3,0,1,2]
counting_sort(array_list)

