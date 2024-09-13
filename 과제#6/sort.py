
def sort_list(obj, inplace=True, ascending=True):
    if inplace == True:
        return obj
    else:
        copy = obj[:]
        if ascending == True:
            copy.sort()
            return copy
        else:
            copy.sort(reverse = True)
            return copy

def sort_dict_by_key(obj, ascending=True):
    l = list(obj.items())
    if ascending == True:
        l.sort(key = lambda x : x[0])
        return l
    else:
        l.sort(key = lambda x : -x[0])
        return l
    

def sort_dict_by_val(obj, ascending=True):
    l = list(obj.items())
    if ascending == True:
        l.sort(key = lambda x : x[1])
        return l
    else:
        l.sort(key = lambda x : x[1], reverse = True)
        return l
    
