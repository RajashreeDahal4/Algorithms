"""
Name: Rajashree Dahal
Date: September 30, 2023
Problem: Fibonacci Series Different Variations
0,0 => 1,1
2,1 => 3,2
4,3 => 5,5
6,8 => 7,13
8,21 => 9,34
"""

def fibonacci_baseline(n):
    '''
    This function executes in exponential time time
    '''
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci_baseline(n-1)+fibonacci_baseline(n-2)
    


def fibonacci_linear(n,values):
    '''
    This function executes in linear time 
    '''
    if values[n]!=-1:
        return values[n]
    elif n==1:
        values[n]=1
        return values[n]
    elif n==2:
        values[n]=1
        return values[n]
    else:
        values[n]=fibonacci_linear(n-1,values)+fibonacci_linear(n-2,values)
        return values[n]


def fibonacci_dependency_graph(n,values):
    '''
    This function executes in linear time
    '''
    values[1]=1
    values[2]=1
    for i in range(3,n+1):
        values[i]=values[i-1]+values[i-2]
    return values[n]
num=9
result=fibonacci_dependency_graph(num,values=[-1]*(num+1))
print(result)