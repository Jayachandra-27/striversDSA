#SELECTION SORT
# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         first_index=i
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[first_index]:
#                 first_index=j
#         arr[i],arr[first_index]=arr[first_index],arr[i]

#     print(arr)


# selection_sort([13,46,24,52,20,9])

#BUBBLE SORT
def bubble_sort(arr):
    for i in range(len(arr)-1,-1,-1):
        did_swap=False
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                did_swap=True
        if not did_swap:
            break
    print(arr)



bubble_sort([13,46,24,52,20,9])