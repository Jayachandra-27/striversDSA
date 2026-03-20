# 1. Largest Element 
# i used selection sort so o(n^2)
# can use sort method o(nlogn)

# def largestElement(self, nums):
#         n=len(nums)
#         for i in range(n-1):
#             k=i
#             for j in range(i+1,n):
#                 if nums[j]<nums[k]:
#                     k=j
#             nums[i],nums[k]=nums[k],nums[i]
#         for le in range(n-1,-1,-1):
#             return (nums[le])
        