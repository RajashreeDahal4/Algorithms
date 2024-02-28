"""
Date: February 28, 2024
Name: Rajashree Dahal
Problem:We want to build baskets and put each of the input fruits into those baskets.
A "basket" is simply some collection of fruits.
We want to build the FEWEST number of baskets, such that each basket has no
more than 1 of the same fruit. 
"""

liss=['a','a','b','c','d','d','a','b','c','a','b','c','d']
def basket(liss):
    dict={i:0 for i in liss}
    counter=0
    dicts={}
    dicts[0]=[]
    for enum,each_element in enumerate(liss):=
        if each_element not in dicts[counter]:
            dicts[counter].append(each_element)
        else:
            tracker=0
            while each_element in dicts[counter]:
                counter=counter+1
                if counter not in dicts.keys():
                    dicts[counter]=[]
                if each_element not in dicts[counter]:
                    dicts[counter].append(each_element)
                    counter=counter+1
                    if counter not in dicts.keys():
                        dicts[counter]=[]
        counter=0
    results=[value for key,value in dicts.items() if value]
    return results
result=basket(liss)  
print("The result is",result)