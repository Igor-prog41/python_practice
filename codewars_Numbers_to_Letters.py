# Given an array of numbers (in string format), you must return a string.
# The numbers correspond to the letters of the alphabet in reverse order: a=26, z=1 etc.
# You should also account for '!', '?' and ' ' that are represented by '27', '28' and '29' respectively.


def switcher(arr):
    #your code here
    list_out = []
    for num in arr:
        if num == "27":
            list_out.append("!")
        elif num == "28":
            list_out.append("?")
        elif num == "29":
            list_out.append(" ")
        else:
            list_out.append(chr(123 - int(num)))
    return "".join(list_out)


test_num = ['24', '12', '23', '22', '4', '26', '9', '8']
print(switcher(test_num))


# for n in range(26):
#     print( f" {n}  for {chr(122 - n) }")  # 1 z
