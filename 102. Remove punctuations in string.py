# 102. Remove punctuations in string
# Example like- I/P: Md 7{-&=Raju @)!;Alam{}- O/P: Md Raju Alam
# 1 way salution

def removepun(name):
    print(f"Original string: {name}")

    for i in name:
        
        if (i>="A" and i<="Z") or (i>="a" and i<="z") or (i==" "):
            
            print(i,end="")

name="Md 7{-&=Raju @)!;Alam{}-"

removepun(name)
