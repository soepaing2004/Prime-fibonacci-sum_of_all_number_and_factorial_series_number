class Student():
    teacher="Su Su" #class attribute
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):  #instance method
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def teacher_info(cls):   #class method
        print(cls.teacher)

    @staticmethod
    def info():    #static method
        print("This is a static method")

s1=Student(34,53,64)
s2=Student(72,46,74)
print(s1.avg())
print(s2.avg())
s1.teacher_info()
s1.info()


class Temperature():
    def __init__(self,x,y):
        self.x=x
        self.y=y


    @staticmethod
    def info():
        a=y*1.8+32
        print("The temperature of "+x+" city in fahrenheit is ",a)

x=input("Enter the name of your city. ")
y=int(input("Enter the "+x+" city temperature in celsius :"))

result=Temperature(x,y)
result.info()