#Merge two sorted arrays into a single, fully sorted array without using Python's built-in .sort() and .sorted() function.

def bubble_sort(arr , n):
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp 

def merge(arr1 , arr2):
    merged_arr = arr1 + arr2
    bubble_sort(merged_arr , len(merged_arr))
    return merged_arr


arr1 = []
arr2 = []
n = int(input("Enter the number of elements in the array1:"))
for i in range(n):
    print("Enter element for array 1:")
    arr1.append(int(input()))

m = int(input("Enter the number of elements in the array2:"))    
for i in range(m):
    print("Enter element for array 2:")
    arr2.append(int(input()))

merged_array = merge(arr1 , arr2)
print("Merged and sorted array: ", merged_array)
