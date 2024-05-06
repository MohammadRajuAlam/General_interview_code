class Father:
    country="india"
    code="+91"

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def get_father(self):
        self.car="yes"
        print(f"Name: {self.name}\nAge: {self.age}\nSex: {self.sex}\n")

    def __account(self): # This is private function
        self.acc="12345678"
        self.__pswd="trg5678" # This is private variable
        self.acc_type="Saving"
        self.balance=568955
        print(f"Account No: {self.acc}\nPasword: {self.__pswd}\nAccount Type: {self.acc_type}\nBalance: {self.balance}\n")

    def get_acc(self):
        return self.__account() # Here We are returning (accessing) private function

    @classmethod
    def get_country(cls):
        print(f"Country Name: {cls.country}\nCountry Code: {cls.code}\n")

    @staticmethod
    def get_f_address(village,city,pincode,district,state):
        print(f"Village Name: {village}\nCity: {city}\nPincode: {pincode}\nDistrict: {district}\nState: {state}\n")

class Daughter(Father):

    def __init__(self,dname,dage,phone,email):
        self.dname=dname
        self.dage=dage
        self.phone=phone
        self.email=email
        super().__init__("Suraj",55,"Male")
        
    def get_daughter(self):
        print(f"Name: {self.dname}\nAge: {self.dage}\nPhone No: {self.phone}\nEmail Id: {self.email}\n")

    def get_d_address(self,area,city,pincode,district,state):
        self.area=area
        self.city=city
        self.pincode=pincode
        self.district=district
        self.state=state
        print(f"Area Name: {self.area}\nCity: {self.city}\nPin Code: {self.pincode}\nDistrict: {self.district}\nState: {self.state}\n")

    @classmethod
    def get_d_country(cls):
        print(f"Country Name: {cls.country}\nPin Code: {cls.code}\n")

    @staticmethod
    def get_d_college(name,clas,roll):
        print(f"College Name: {name}\nClass: {clas}\nRoll No: {roll}\n")
        

obj2=Daughter("Rakhi",25,8897568874,"rakhi@gmail.com")
# Here Access Child class properties
#obj2.get_daughter()
#obj2.get_d_address("Ansar Nagar","Nawada",805105,"Nawada","Bihar")
#obj2.get_d_country()  
#Daughter.get_d_country()
#obj2.get_d_college("Gandhi Inter College","BSc",156)
#Daughter.get_d_college("Gandhi Inter College","BSc",156)

#Here Accessing Super class properties using subclass
#obj2.get_father()
#obj2.__account() # We can't access bcz this is private function
#obj2.get_acc()
#obj2.get_country()
#Daughter.get_country()
#obj2.get_f_address("Main Panchu","Hisua",805103,"Nawada","Bihar")
Daughter.get_f_address("Main Panchu","Hisua",805103,"Nawada","Bihar")
