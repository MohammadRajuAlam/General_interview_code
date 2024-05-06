# 104. Reverse the Element of List
# 1 way salutions
'''
def rev(lst):
    print(f"Original list:\n{lst}")
    #print(lst[::-1]) # using slice to reverse of list

    empty=[]

    l=len(lst)

    for i in range(l-1,-1,-1):
        
        empty.append(lst[i])

    print(f"After Reverse of list:\n{empty}")

ls=[50,40,20,60,10,0]

rev(ls)
'''
# 2nd way salutions without using append () Here using Bubble sort

def rev(lst):
    print(f"Original List:\n{lst}")

    l=len(lst)

    for i in range(l//2):

        lst[i], lst[l-i-1] = lst[l-i-1], lst[i] # Here Swapping the element

    print(f"After Reverse of List:\n{lst}")
    
ls=[50,40,20,60,10,0]

rev(ls)
