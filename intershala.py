# To check whether the given series is same as series define below
# f(0) = 0
# f(1) = 1 
# f(n) = 2*lst[n-1] - 2*lst[n-2]

def is_seq(lst):
    lst_length = len(lst)
    flag = False
    print(lst_length)
    if lst_length == 1 and lst[0] == 0 :
            flag = True
    if lst_length == 2 and lst[1] == 1 :
        flag = True
    for i in range(2,lst_length):
        if lst[i] == 2*lst[i-1] - 2*lst[i-2] :
            flag = True
        else:
            flag = False
            break
    return flag


lst = [0,1,2,2,0,-4,-8,-8,0,16]
print(is_seq(lst))

#To generate the sequence
''' lst = [0,1]
for i in range(2,10):
    n = 2*lst[i-1] - 2*lst[i-2]
    lst.append(n)

print(*lst)
'''    
