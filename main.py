#challenge1

# Python 3 program to find 
# factorial of given number
  
# Function to find factorial of given number
def factorial(n):
       
    if n == 0:
        return 1
      
    return n * factorial(n-1)
   
# Driver Code
num = 5;
print("Factorial of", num, "is",
factorial(num))



# Python program to check if year is a leap year or not

year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))



#challenge2

class BankAccount:
  def __init__(self, account_number: str, account_holder_name: str, account_balance: float):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = account_balance

  def deposit(self, amount: float):
      self.__account_balance += amount

  def withdraw(self, amount: float):
      if amount > self.__account_balance:
          print("Insufficient balance")
      else:
          self.__account_balance -= amount

  def display_balance(self):
      print("Account Balance:", self.__account_balance)

# Create an instance of the BankAccount class
bank_account = BankAccount("1234567890", "John Doe", 1000.0)

# Test deposit and withdrawal functionality
bank_account.deposit(500.0)
bank_account.withdraw(200.0)
bank_account.display_balance()




class Player:
  def play(self):
      print("The player is playing cricket.")

class Batsman(Player):
  def play(self):
      print("The batsman is batting.")

class Bowler(Player):
  def play(self):
      print("The bowler is bowling.")

# Create objects of both the Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()


#challenge3

def linear_search_product(products, target):
  indices = []
  for i in range(len(products)):
      if products[i] == target:
          indices.append(i)
  return indices

products = ['apple', 'banana', 'orange', 'banana']
target = 'banana'
indices = linear_search_product(products, target)
print(indices)



def sort_students(students):
  students.sort(key=lambda x: x.cgpa, reverse=True)

# Define a Student class
class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

# Create a list of Student objects
students = [
  Student("John Doe", "001", 3.5),
  Student("Jane Smith", "002", 3.8),
  Student("Bob Johnson", "003", 3.2),
]

# Sort the list of students by CGPA in descending order
sort_students(students)

# Print the sorted list of students
for student in students:
  print(f"{student.name} ({student.roll_number}): {student.cgpa}")

