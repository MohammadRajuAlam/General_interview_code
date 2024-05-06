# Example 1: Using items() function
# wap to display cricket player name with matches and made scored and total scored
'''
def cricket(name="", **kwargs):
    print(f"Name of player: {name}")

    dic={}
    
    total=0
    
    for k, v in kwargs.items():
        
        dic[k]=v # Here Assining values by keys
        
        total=total+kwargs[k] # Here Adding every value in total by key

    print(dic)
    print(f"Total Runs: {total} in {len(kwargs)} matches")

cricket("Rohit", m1=50,m2=30,m3=6)

# Example 2: Using keys() function

def cricket(name="", **kwargs):
    print(f"Name of player: {name}")

    dic={}
    
    total=0
    
    for k in kwargs.keys():
        
        dic[k]=kwargs[k] # Here Assining values by using object name with key
        
        total=total+kwargs[k] # Here Adding every value in total by key

    print(dic)
    print(f"Total Runs: {total} in {len(kwargs)} matches")

cricket("Virat", m1=100,m2=90,m3=60, m4=20)
'''
# Programs
# wap to display subject with marks in using dict

dic={"python":98, "c":80,"c++":86,"java":75, "php":93}
total=0

for k, v in dic.items(): # OR for k in dic.keys():

    total=total+dic[k]
    print(f"{k}: {v}")
    
print(f"Total Marks: {total}")

# wap to asked num of subject from users and display subject, marks, total marks and total (len) subject

dic={}

num=int(input("Enter the num of sub\n"))

total=0

for i in range(num):
    
    sub=input("Enter the subject\n")
    marks=int(input("enter the marks\n"))
    
    dic[sub]=marks
    
    total=total+dic[sub]

print(dic)
print(f"Total sub are {len(dic)}")
print(f"Total marks: {total}")

