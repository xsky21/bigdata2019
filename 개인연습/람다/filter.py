def positive(number_list):
    result = []
    for num in number_list:
        if num > 0:
            result.append(num)
    return result

print(positive([1,-3,2,0,4,-7]))
