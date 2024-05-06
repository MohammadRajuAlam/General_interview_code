# 103. Reverse of String
# Example like- I/P: Md Raju Alam O/P: malA ujaR dM
# 1 way salution
'''
def reverse(name):
    print(f"Original str:\n{name}\n")

    empty=""
    for i in name:
        empty=i+empty

    print(f"Reverse String:\n{empty}")

name=input("Enter the name\n")

reverse(name)
'''

# 2nd way salution

def rev(name):
    print(f"Original str:{name}\n")

    l=len(name)
    for i in range(l-1,-1,-1):
        
        print(name[i],end="")

name="Bangalore"

rev(name)
