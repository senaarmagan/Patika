def nested_reverse(input_list):
    if type(input_list) == list:
        return [nested_reverse(x) for x in input_list[::-1]]
    else:
        return input_list
    
input_list = [[1, 2], [3, 4], [5, 6, 7]] 
output = nested_reverse((input_list))
print(output) 