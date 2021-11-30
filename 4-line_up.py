#!/usr/bin/env python3
def add_arrays(arr1, arr2):
    """ Add 2 arrays of the same size  """
    if len(arr1) != len(arr2):
        return None
    
    result = [0 for x in range(len(arr1))]

    for i in range(len(arr1)):
            result[i] = arr1[i] + arr2[i]
    
    return result