def migratoryBirds(arr):
    frequencies = [0] * 6
    for ele in arr:
        frequencies[ele] += 1
 
    max_val = 0
    max_idx = 5
     
    for idx in range(5, 0, -1):
        if frequencies[idx] >= max_val:
            max_idx = idx
            max_val = frequencies[idx]
 
    return max_idx
