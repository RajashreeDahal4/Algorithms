"""
Date: March 1, 2024
Name: Rajashree Dahal
Problem:
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.
"""
def arrayManipulation(n, queries):
    # Write your code here
    result=[0]*n
    print(result)
    for each_query in queries:
        start=each_query[0]
        end=each_query[1]
        value=each_query[2]
        result=[(i+value) if (enum<=(end-1) and enum>=(start-1)) else i for enum,i in enumerate(result)]

    return max(result)