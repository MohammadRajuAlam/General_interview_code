# Remove Space in string
# 1 way salution

def removespace(name):
    print(f"Before Remove string: {name}")
    
    for i in name:

        if i==" ":
            continue
        
        print(i,end="")

name=input("Enter the name with space\n")

removespace(name)


# 2 way salution

def rmvspace(name):
    print(f"Before Remove String: {name}")
    l=len(name)

    for i in range(l):
        if name[i]==" ":
            continue

        print(name[i],end="")

name=input("Enter the name with space\n")
rmvspace(name)
