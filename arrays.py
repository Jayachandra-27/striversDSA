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
        
# 2.Second Largest Element

# def secondLargestElement(self, nums):
#         largest=float('-inf')
#         second_largest=float('-inf')
#         for i in nums:
#             if i>largest:
#                 second_largest=largest
#                 largest=i
#             elif i>second_largest and i!=largest:
#                 second_largest=i
#         if second_largest==float('-inf'):
#             return -1
#         return second_largest


# 3.Check if the Array is Sorted II
# def isSorted(self, nums):
#         n=len(nums)
#         for i in range(n-1):
#             if nums[i]>nums[i+1]:
#                 return False
#         return True

#4. Remove duplicates from sorted array
# def removeDuplicates(nums):
#         i=0
#         j=1
#         while j<len(nums):
#             if nums[i]!=nums[j]:
#                 i+=1
#                 nums[i]=nums[j]
#             j+=1
            
#         return (nums,i+1)
# print(removeDuplicates([0, 0, 3, 3, 5, 6]))