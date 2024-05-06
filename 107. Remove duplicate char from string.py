# 107. Remove duplicate char from string
# 1 way salution
'''
def remvdpl(name):
    print(f"Original string:\n{name}")

    empty=""
    for i in name:
        
        if i not in empty:
            
            empty=empty+i

    print(f"After remove duplicat char:\n{empty}")

name="aaabbaaccddd"

remvdpl(name)
'''

# 2nd way salution

def rev(name):
    print(name)

    l=len(name)
    empty=""
    for i in range(l):
        if name[i] not in empty:
            empty=empty+name[i]
            print(f"{name[i]}",end="")
    
    #print(empty)

name="aabbcsscaad"

rev(name)
