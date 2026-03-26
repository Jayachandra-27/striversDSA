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

# 8.Maximum Consecutive Ones
# def findMaxConsecutiveOnes(nums):
#     max1=0
#     j=0
#     c=0
#     while j<len(nums):
#         if nums[j]==1:
#             c+=1
#         else:
#             max1=max(max1,c)
#             c=0
#         j+=1
#     max1=max(max1,c)
#     return max1



# print(findMaxConsecutiveOnes([1,1,0,1,1,1]))

# 9.Find the number that appears once, and other numbers twice.

# def singleNumber(nums):
#     res=0
#     for i in nums:
#         res=res^i
#     return res
# print(singleNumber([1, 2, 2, 4, 3,3,5, 1, 4]))

#10.
# def longestSubarray(nums, k):
#     i=0
#     j=0
#     sum=0
#     maxsum=0
#     while j<(len(nums)):
#         if nums[j]<k:
#             sum+=nums[j]
#             j+=1
            
#         else:

        
        

# # print(longestSubarray([10, 5, 2, 7, 1, 9],15))
# print(longestSubarray([12,7,15,3,1,9],13))

# 11.Merge two sorted arrays
# def merge(nums1, m, nums2, n):
#         k=m+n-1
#         i=m-1
#         j=n-1
#         while i>=0 and j>=0:
#             if nums1[i]<nums2[j]:
#                 nums1[k]=nums2[j]
#                 j-=1
#                 k-=1
#             elif nums1[i]>=nums2[j]:
#                 nums1[k]=nums1[i]
#                 i-=1
#                 k-=1
#         while i>=0:
#             nums1[k]=nums1[i]
#             i-=1
#             k-=1
#         while j>=0:
#             nums1[k]=nums2[j]
#             j-=1
#             k-=1
#         return nums1
# print(merge([1,2,3,0,0,0],3,[2,5,6],3))

# 12.---977. Squares of a Sorted Array
# def sortedSquares(nums):
#         neg_list=[]
#         pos_list=[]
#         neg_rev_list=[]
#         final_list=[]
#         for i in nums:
#             if i>=0:
#                 pos_list.append(i**2)
#             else:
#                 neg_list.append(i**2)
#         for i in range(len(neg_list)-1,-1,-1):
#             neg_rev_list.append(neg_list[i])
#         if len(neg_list)==0:
#             return pos_list
#         if len(pos_list)==0:
#             return neg_rev_list
#         i=0
#         j=0
#         k=0
#         while i<len(neg_rev_list) and j<len(pos_list):
#             if neg_rev_list[i]<pos_list[j]:
#                 final_list.append(neg_rev_list[i])
                
#                 i+=1
#             else:
#                 final_list.append(pos_list[j])
                 
#                 j+=1
#         while i<len(neg_rev_list):
#             final_list.append(neg_rev_list[i])
             
#             i+=1
#         while j<len(pos_list):
#             final_list.append(pos_list[j])
             
#             j+=1
#         return final_list
# print(sortedSquares([-4,-1,0,3,10]))

# 13.----15. 3Sum
# def threeSum(nums):
#         nums.sort()
#         l=[]
#         for i in range(len(nums)-2):
#             if i>0 and nums[i]==nums[i-1]:
#                 continue
#             left=i+1
#             right=len(nums)-1
#             asum=-1*nums[i]
#             while left<right:
#                 c_sum=nums[left]+nums[right]
#                 if asum==c_sum:
#                     l.append([nums[i],nums[left],nums[right]])
#                     left+=1
#                     right-=1
#                     while left<right and nums[left]==nums[left-1]:
#                         left+=1
#                     while left<right and nums[right]==nums[right+1]:
#                         right-=1
#                 elif c_sum<asum:
#                     left+=1
#                 else:
#                     right-=1
#         return l
# print(threeSum([-1,0,1,2,-1,-4]))

# 14.----16. 3Sum Closest
def threeSumClosest(nums, target):
        nums.sort()
        close= nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            
            left=i+1
            right=len(nums)-1
            
            while left<right:
                c_sum=nums[i]+nums[left]+nums[right]
                if abs(c_sum - target) < abs(close - target):
                    close = c_sum
                    
                elif c_sum<target:
                    
                    left+=1
                elif c_sum > target:
                    right -= 1
                else:
                    return c_sum
        return close
print(threeSumClosest([-1,2,1,-4],1))

# 2 sum with duplicates in array
def twoSumDup(arr,target):
    n=len(arr)
    left=0
    right=n-1
    l=[]
    while left<right:
        s=arr[left]+arr[right]
        if s==target:
            l.append([arr[left],arr[right]])
            left+=1
            right-=1
            while arr[left]==arr[left-1]:
                left+=1
            while arr[right]==arr[right+1]:
                right-=1
        elif s<target:
            left+=1
        else:
            right-=1
    return l
    



               
print(twoSumDup([0,1,1,1,2,2,3,3,3,4,4,5],5)) 

