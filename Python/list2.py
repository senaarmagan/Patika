def flatten_list(input_list):
    flat_list = []
    
    for item in input_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    
    return flat_list

input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output = flatten_list(input_list)
print(output)
