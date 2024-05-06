# 109. Remove duplicat element from list

# 1 way salution
'''
def remv(lst):
    print(f"original list:\n{lst}")

    empty=[]
    
    for i in lst:
        if i not in empty:
            empty.append(i)

    print(f"After Removed element:\n{empty}")

ls=[5,10,5,20,5,10,5]

remv(ls)
'''

# 2nd Way salution

def rem(lst):
    print(f"Original list:\n{lst}")

    l=len(lst)

    empty=[]

    for i in range(l):
        if lst[i] not in empty:
            empty.append(lst[i])
            
    print(f"After remove element:\n{empty}")

ls=[5,10,5,20,5,10,5]

rem(ls)

