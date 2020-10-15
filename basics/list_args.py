n = int(input())
a=[]
for _ in range(n):
    args = input().split()
    operation, arr_ind_ele = args[0], args[1:]
    
    if operation != 'print':
        operation += "("+ ",".join(arr_ind_ele)+")"
        eval("a."+operation)
    else:
        print(a)
