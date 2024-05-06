# 106. Find 2nd or 3rd Max or any num from list
# 1 way salution
'''
def sort(lst):
    print(f"Original List:\n{lst}")
    #lst.sort() # Using Builtin method of list
    #print(lst) # OR
    srt=sorted(lst) # Using sorted builtin function of python
    print(srt)

ls=[10,20,5,60,30,70,0]

sort(ls)
'''
# 2nd way salution

def sor(lst):
    print(lst)

    l=len(lst)

    for i in range(l):
        for j in range(0, l-i-1):
            
            if lst[j] > lst[j+1]:

                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(lst)
    print(lst[-2]) # Finding 2nd Max in list

ls=[10,20,5,60,30,70,0]

sor(ls)

