"""
Date: October 3, 2023
Name: Rajashree Dahal
Problem: 
Design a divide-and-conquer algorithm, in pseudo-code to compute a^n in o(n)-time (little-o). 
Please also analyze your running time, where you consider a multiplication as a basic operation. (20pts)
"""
def a_power_n(a,power_value):
    print(a,power_value)
    if power_value==0:
        return 1
    elif power_value==1:
        return a 
    else:
        mid_value=int(power_value/2)
        left_prod=a_power_n(a,mid_value)
        right_prod=a_power_n(a,power_value-mid_value)
        result=left_prod*right_prod
        return result
a=4
power_value=4
result=a_power_n(a,power_value)
print("result: ",result)