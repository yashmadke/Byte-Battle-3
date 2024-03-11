''' Write a program to find the middle element of the list. If the list contains an even number
of elements, return the second middle element '''

def find_middle(lst):
    length = len(lst)
    if length % 2 == 1:
        return lst[length // 2]
    else:
        return lst[length // 2]

test_list_1 = [1, 2, 3, 4, 5]
test_list_2 = [1, 2, 3, 4, 5, 6]

print("Middle element(s) of test_list_1:", find_middle(test_list_1))
print("Middle element(s) of test_list_2:", find_middle(test_list_2))