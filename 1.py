# Day1: Write a function that takes an array of integers and returns the indices of the two numbers that add up to a specific target.

def TwoSum(num , target):
    for i in num:
        for j in num:
            if i + j == target:
                return (num.index(i), num.index(j))
    return None

Target = int(input("Enter the target number : "))
num = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
print(TwoSum(num , Target))