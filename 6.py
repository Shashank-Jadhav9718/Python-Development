#Write a program that removes all duplicate elements from a list manually without converting the list into a set()

messy_list = [1, 2, 2, 3, "apple", "apple", 4, 5, 1]
print("Original list: ", messy_list)

def remove_duplicates(lst):
    char_count = {}
    processed_list = []
    for char in lst:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            if char_count[char] == 1  and char not in processed_list:
                processed_list.append(char)
    return processed_list

def remove_duplicates_alternative(lst):
    unique_list = []
    for char in lst:
        if char not in unique_list:
            unique_list.append(char)
    return unique_list


def remove_duplicates_using_set(lst):
    return list(set(lst))

result = remove_duplicates(messy_list)
print("List after removing duplicates: ", result)   

result_set = remove_duplicates_using_set(messy_list)
print("List after removing duplicates (using set): ", result_set)   

result_alternative = remove_duplicates_alternative(messy_list)
print("List after removing duplicates (alternative method): ", result_alternative)
