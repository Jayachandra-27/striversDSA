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

# 5.Move zeros to end
# def moveZeroes(nums):
#         i=0
#         j=0
#         while j<len(nums):
#             if nums[j]!=0:
#                 nums[i]=nums[j]
#                 i+=1
#             j+=1
#         for k in range(i,len(nums)):
#              nums[k]=0
             
#         return nums
# print(moveZeroes([0, 20, 0, -20, 0, 20]))

# 6.Left Rotate the Array by One
# def rotateArrayByOne(nums):
#         first_ele=nums[0]
#         i=0
#         for j in range(1,len(nums)):
#             nums[i]=nums[j]
#             i+=1
#         nums[len(nums)-1]=first_ele
#         return nums
# print(rotateArrayByOne([-1, 0, 3, 6]))


#6.Rotate from right by k steps
# def rotate(nums,k):
#     k = k % len(nums)
#     i=len(nums)-1
#     h=len(nums)-1
#     temp_arr=[]
#     c=k
#     while c>0:
#         temp_arr.append(nums[i])
#         i-=1
#         c-=1
#     while i>=0:
#         nums[h]=nums[i]
#         h-=1
#         i-=1
#     for j in range(len(temp_arr)):
#         nums[h]=temp_arr[j]
#         h-=1
#     return nums
# print(rotate([1,2,3,4,5,6,7],3))

# 7.Union of Two Sorted Arrays
# def unionArray( nums1, nums2):
#     d={}
#     l=[]
#     for i in nums1:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
#     for j in nums2:
#         if j in d:
#             d[j]-=1
#         else:
#             d[j]=1
#     for k,v in d.items():
#         l.append(k)

#     return l
        
    
# print(unionArray([1,2,3,4,5],[2,3,4,4,5]))

def findMaxConsecutiveOnes(nums):
    max1=0
    j=0
    c=0
    while j<len(nums):
        if nums[j]==1:
            c+=1
        else:
            max1=max(max1,c)
            c=0
        j+=1
    max1=max(max1,c)
    return max1



print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
