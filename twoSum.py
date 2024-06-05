from typing import List

""" Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order."""

def TwoSum(num: List[int],target: int):
    for i in num:
        if target-i in num: return True
    return False

if __name__== "__main__":
    # num = [2,7,11,15]
    # target = 16
    # print(TwoSum(num,target)) # Output: True
    pass