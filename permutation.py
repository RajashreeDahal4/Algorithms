#given a number from 1 to n, find the arrangement of number from 1 to n taken n at a time

def permutation(n,perm):
    '''
    This is a function to do permutation by recursion
    '''
    if len(perm)==n:
        print(perm)
        return
    else:
        for i in range(1,n+1):
            if i not in perm:
                perm.append(i)
                permutation(n,perm)
                perm.pop()
perm=[]
permutation(4,perm)
