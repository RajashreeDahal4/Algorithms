'''
Date: September 23,2023
find the number of possible steps to move plates in a tower of hanoi problem
'''

def hanoi_steps(n,original,intermediate,destination):
    if n==1:
        print(f"move the plate {n} from {original} to {destination}")
    else:
        hanoi_steps(n-1,original,destination,intermediate)
        print(f"move the plate {n} from {original} to {destination}")
        hanoi_steps(n-1,intermediate,original,destination)

hanoi_steps(3,"tower1","tower2","tower3")
