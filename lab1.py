
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    max_num=0
    if int_list == []:
        return None
    if int_list==None:
        raise ValueError("list equals None")
    for i in range(len(int_list)):
        if i == 0:
            max_num=int_list[i]
        if int_list[i]>max_num:
            max_num=int_list[i]
    return max_num

def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list==None:
        raise ValueError("list equals None")
    if len(int_list)<=1:
        return int_list
    else:
        return [int_list[-1]]+reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list== None:
        raise ValueError("list equals None")
    else:
        mid=int((low+high)/2.0)
        if int_list[mid]==target:
            return mid
        elif target > int_list[mid]:
            return bin_search(target,mid+1,high,int_list)
        elif target < int_list[mid]:
            return bin_search(target,low,mid-1,int_list)
