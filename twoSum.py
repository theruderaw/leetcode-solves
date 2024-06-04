from typing import List

def TwoSum(num: List[int],target: int):
    for i in num:
        if target-i in num: return True
    return False

if __name__== "__main__":
    # num = [2,7,11,15]
    # target = 16
    # print(TwoSum(num,target)) # Output: True
    pass