'''
Date: September 23, 2023
Task: find all the possible subsets of sets from number 1 to n.
'''

def subsets(i,subset):
    #baseline condition
    if i>4:
        print(subset)
        return
    else:
        subset.append(i)
        subsets(i+1,subset)
        subset.pop()
        subsets(i+1,subset)


subsets(1,subset=[])

