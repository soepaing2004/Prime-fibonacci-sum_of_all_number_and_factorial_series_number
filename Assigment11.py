class Operation():
  #  def __init__(self,user_input):
     #   self.x=user_input

    @staticmethod
    def factorial_number():
        factorial=int(input("Enter a number that you want his factorial series number:"))
        unknown_number_for_factorial=1
        for i in range(2,factorial+1):
             unknown_number_for_factorial=i*unknown_number_for_factorial
             print(unknown_number_for_factorial)

    @staticmethod
    def fibonacci_number():
        fibonacci=int(input("Enter a number that you want his fibonacci serial number"))
        unknown_number1_for_fibonacci=0
        unknown_numbmer2_for_fibonacci=1
        for i in range(0,fibonacci):
            print(unknown_number1_for_fibonacci)
            unknown_number3_for_fibonacci=unknown_numbmer2_for_fibonacci+unknown_number1_for_fibonacci
            unknown_number1_for_fibonacci=unknown_numbmer2_for_fibonacci
            unknown_numbmer2_for_fibonacci=unknown_number3_for_fibonacci

    @staticmethod
    def sum_of_the_number():
        sum_number=int(input("Enter a number that you want his sum of all number from 0:"))
        unknown_number_for_sum_number=0
        for i in range(1,sum_number+1):
            unknown_number_for_sum_number=unknown_number_for_sum_number+i
            print(unknown_number_for_sum_number)

    @staticmethod
    def prime_number():
        prime=int(input("Enter a number to check that is a prime number or not:"))
        unknown_number_for_prime_number=0
        if (prime==1):
            print(prime,"is not a prime number.")
        else:
            for i in range(2,prime):
                if(prime%i==0):
                    unknown_number_for_prime_number+=1
                    break
            if (unknown_number_for_prime_number==1):
                print(prime," is not a prime number.")
            else:
                print(prime," is a prime number.")


print("This is a program that's calculate about the factorial number,fibonacci number, the sum of all the that you enter from 0 and prime number.")
user_input=input("Enter your operation:")
#Operation(user_input)
if user_input.lower()=="factorial":
    Operation.factorial_number()
elif user_input.lower()=="fibonacci":
    Operation.fibonacci_number()
elif user_input.lower()=="sum":
    Operation.sum_of_the_number()
elif user_input.lower()=="prime":
    Operation.prime_number()
else:
    print("There's no operation that you enter.")
