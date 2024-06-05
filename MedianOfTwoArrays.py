"""Given two sorted arrays nums1 and nums2 of size m and n respectively,
 return the median of the two sorted arrays."""

def MedianOfTwoSortedArrays(arr1,arr2):
    arr1.extend(arr2)
    arr1.sort()
    n = len(arr1)
    if n % 2 == 0:
        return (arr1[n//2 - 1] + arr1[n//2]) /2
    else :
        return arr1[n//2]

if __name__ == "__main__":
    arr1 = [1,3,5,7,9]
    arr2 = [2,4,6,8,10]
    print(MedianOfTwoSortedArrays(arr1,arr2))
    