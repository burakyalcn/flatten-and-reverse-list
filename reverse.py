from re import L


input = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(l):
    for i in l:
        if isinstance(i,list):
            i.reverse()
    l.reverse()    
    return l

print(reverse_list(input))
