"""
Date: September 23, 2023
task: find the maximum continuous subarry sum of a given array without using recursion
"""
#Approach
def MSE(given_list):
    # max_value=given_list[0]
    # sum_val=given_list[0]
    max_value,sum_val=0,0
    for k,_ in enumerate(given_list):
        sum_val=max(given_list[k],sum_val+given_list[k])
        max_value=max(max_value,sum_val)
    print(max_value)
MSE([-1,2,4,-3,5,2,-5,2])


    


