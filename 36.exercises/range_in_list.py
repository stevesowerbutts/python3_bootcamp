def range_in_list(start=0, end=None):
    '''
    Accepts a list, start and end indices and returns the sum of the values
    between.
    
    '''
    if end:
        end += 1
    return sum(list_to_sum[start:end])



range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
