def flat_arrays(arr): 
    flat_list = []
    for item in arr:
        if type(item) == list:
            flat_list = flat_list + flat_arrays(item)
        else:
            flat_list.append(item)
    return flat_list