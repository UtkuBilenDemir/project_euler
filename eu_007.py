# https://projecteuler.net/problem=7

p_list = [2]
k = 3
while len(p_list) < 10002:
    k_o = k
    i = 0
    while k_o>1 and i<len(p_list):
        if not k_o%p_list[i]:
            k_o /= p_list[i]
        else:
            i += 1
    if k_o == k:
        p_list.insert(0, k)
    k += 1

print(p_list[-10001])
        
        
    
    
    