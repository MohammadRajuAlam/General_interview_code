# 108. Count (Accurance) char in string
# 1 way salution

# 2nd way salution

def rev(name):
    print(name)

    l=len(name)
    empty=""
    for i in range(l):
        if name[i] not in empty:
            empty=empty+name[i]
            print(f"{name[i]}={name.count(name[i])}")
    
    #print(empty)

name="aabbcsscaad"

rev(name)
