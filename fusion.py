import time
T1 = [1,1,4,5,6,6]
T2 = [1,2,3,6,7,8,9, 10]

def fusion (T1, T2): 
    T3 = [] 
    i = 0
    j = 0
    while i < len(T1) and j < len(T2):
        if T1[i] < T2[j]:
            T3.append(T1[i])
            i += 1
        else:
            T3.append(T2[j])
            j += 1 
    T3 += T1[i:]
    T3 += T2[j:]
    return T3
    
T = [9 , 5 , 2 , 1 , 0 , 8 , 7]


