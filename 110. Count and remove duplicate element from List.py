# 110. Remove and count duplicat element from list

# 1 way salution
'''
def count(lst):
    print(f"Original List:\n{lst}")

    empty=[]
    for i in lst:
        if i not in empty:
            empty.append(i)
            print(f"{i}= {lst.count(i)}")

    print(f"After Removed duplicate element:\n{empty}")

ls=[40,20,40,5,40,5,10]

count(ls)
        
'''
# 2nd way salution

def count(lst):
    print(f"Original list\n{lst}")

    empty=[]
    l=len(lst)

    for i in range(l):
        if lst[i] not in empty:
            empty.append(lst[i])
            print(f"{lst[i]}= {lst.count(lst[i])}")

    print(empty)

ls=[40,20,40,5,40,5,10]

count(ls)
