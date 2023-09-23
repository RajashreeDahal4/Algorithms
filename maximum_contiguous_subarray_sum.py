"""
Date: September 23, 2023
task: find the maximum continuous subarry sum of a given array without using recursion
"""
#Approach A: Without Using Recursion
def MSE(given_list):
    max_value,sum_val=0,0
    for k,_ in enumerate(given_list):
        sum_val=max(given_list[k],sum_val+given_list[k])
        max_value=max(max_value,sum_val)
    print(max_value)
MSE([-1,2,4,-3,5,2,-5,2])

#Approach B: With Recursion
def MSE_recursion(subarray,si,ei):
    if si==ei:
        return subarray[si]
    else:
        mid_point=int((si+ei)/2)
        left_sum=MSE_recursion(subarray,si,mid_point)
        right_sum=MSE_recursion(subarray,mid_point+1,len(subarray)-1)
        """
        This approach gives rise to three sub cases:
        Case A: the max sum lies in the left half of the array
        Case B: the max sum lies in the right half of the array
        Case C: the max sum also considers the boundary portion as well
        """
        cross_sum=0
        left_max=float('-inf')
        #here moving from left to right
        for i in subarray[mid_point+1:ei]:
            cross_sum=cross_sum+subarray[i]
            if cross_sum>left_max:
                left_max=cross_sum 
        cross_sum=0
        right_max=float('-inf')
        #here moving from right to left
        for enum,i in enumerate(subarray[si:mid_point]):
            # print(mid_point-enum)
            cross_sum=cross_sum+subarray[mid_point-enum]
            if cross_sum>right_max:
                right_max=cross_sum
    return max(left_sum,right_sum,left_max+right_max)

    
subarray=[-1,2,4,-3,5,2,-5,2]
result=MSE_recursion([-1,2,4,-3,5,2,-5,2],0,len(subarray)-1)
print(result)
