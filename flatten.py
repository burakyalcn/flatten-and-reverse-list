input = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output = []
def flatten(l):
    for eleman in l:
        if isinstance(eleman,list):
            flatten(eleman)
        else:
            output.append(eleman)
           
                           
flatten(input) 
print(output)          