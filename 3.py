# Take a list of integers and move all zeros to the end of the list while maintaining the relative order of the non-zero elements.

list = [0, 1, 0, 3, 12]

def moveZerosToEnd(lst):
    for i in list :
        if i == 0:
            list.remove(i)
            list.append(0)
    return list 

print("Original list : ", list)
print("List after moving zeros to the end : ", moveZerosToEnd(list))