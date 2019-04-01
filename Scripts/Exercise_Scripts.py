#Question 1
#Celsius to Fahrenheit formula
#(°C × 1.8) + 32 = °F or in plain English, Multiple by 9, then divide by 5, then add 32.
    
Celsius= int  #Input Value for Celsius
def ConvertCelsius_to_F(Celsius):
"""
Docstring
This function converts Celsius degrees to Fahrenheit. The input in brackets is in Celsius. 

"""
    Fahrenheit = (Celsius * 1.8) + 32 #Converting Celsius to Fahrenheit
    print("%.1f degree celsius is equal to %.1f degree Fahrenheit" %(Celsius, Fahrenheit))#print the Fahrenheit calculation results 
    
#Question 2
    #To calculate BMI:
    #1. Multiply your height in meters (m) by itself 
    #2. Divide your weight in kilograms (kg) by your step 1 result
    
Height = float #input Height value in meters
Weight = int #input weight value in kgs

def Calculate_BMI(Height,Weight):
"""
Docstring
This function calculates the BMI of an individual given the Height in meters and Weight in Kilograms. Calculate_BMI (Height, Weight).

"""
    BMI= Weight / (Height * Height)
    print("Body Mass index= %s" %BMI)
    
#Question 3 Create a program that asks the user to enter their name and their age 
    #And will Print out a message addressed to them that tells them the year that they will turn 100 years old.
    Name= str(input(prompt= \"Enter your name:\"))  # input name here
    Age = int(input(prompt= \"Enter your age:\")) # input age. Defined as an integer. Can only take integer value
    Age_in_100years= (100 - Age) + 2019
    print('Hi,%s' %Name, 'the year will be %d' % Age_in_100years, 'when you are 100 years old')
    
#Question 4 Write a function called fizz_buzz that takes a number.\n",
           # If the number is divisible by 3, it should return “Fizz
           #- If it is divisible by 5, it should return “Buzz”.\n",
            #- If it is divisible by both 3 and 5, it should return “FizzBuzz”.\n",
           #Otherwise, it should return the same number\n",
x =float

def fizz_buzz(x):
"""
Docstring:
This function checks if an input (x)- is divisible by 3 (Gives output "Fizz") or 5 (Gives output "Buzz") . It also checks if it is divisible by both 3 and 5 
(Gives output "FizzBuzz").
"""
    if (x % 3 == 0): 
         print("Fizz")
    if (x % 5 == 0):
         print("Buzz")
    if (x % 3 == 0) and (x % 5 == 0):#If it is divisible by both 3 and 5
         print("FizzBuzz") #print output if it is divisble by both 3 and 5
    else :
        print ("Original number %.1f" % x) #print the original number if its not divisible by 3 and 5
        
#Question 5. Write a function for checking the speed of drivers. This function should have one parameter: speed.
    # If speed is less than 70, it should print “Ok”.\n",
    #Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. 
    #For example, if the speed is 80, it should print: “Points: 2
    #If the driver gets more than 12 points, the function should print: “License suspended
speed = 140
def Speedfunc(speed): #Speed function that takes in one parameter (speed)
"""
This function checks for speed . If speed is below 70 it outputs "Ok". It gives demerit points if speed goes above 70 point and adds a point for every 5km exceeded . If the demerit points are
above 12 , it outputs "License suspended"
"""
    if speed < 70: #This is a condition that will output "OK" only if speed is less than 70
        print('OK') 
    else:
        demerit_point = (speed-70)*(1/5)
    if demerit_point < 12:
         print("Demerit point= %d" %demerit_point)
    else:
         print('License suspended')

#Question 6 
    #Maxfunction compares two given numbers and outputs the number with the greater value.
x= int
y = int
# X and Y declared as integers. Any integer value can be put in.
def maxfunction(x,y):  
"""
Compares two numbers and outputs the one with the greater value
"""
    if x > y: #Comparing value in x to y. If x is greater than y then x is printed as the maximum value
        print("Maximum value= %d" % x)
    if y > x: #Comparing value in y to x. If y is greater than x then y is printed as the maximum value
        print("Maximum value = %d" % y)
#Question 7
#Write a function called showNumbers that takes a parameter called limit. It should print all the numbers 
    #between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print
limit =int #Declaring limit as any integer value
def ShowNumbers(limit):
"""
Prints all prime numbers between 0 and a given limit.
"""
    for i in range(limit+1): #Range function to include the number placed in as limit.
        if (i % 2 == 0):
            print('%d Even No' %i) #Ouputs all Even numbers 
        else:
            print('%d Odd No' %i) #Outputs all Odd numbers
#8. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
    #For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
limit = int #Declaring limit as any number as long as it is an integer
mutiples= [] #Initializing an empty list 
def Sum_mutiples(limit): 
"""
This function sums all the mutiples of 3 and 5 given a certain limit on the inputs
"""
    for i in range (limit+1):
        if (i % 3 == 0): 
            mutiples.append(i) #Appends all the mutiples of 3 to the empty list [mutiples]
        elif (i % 5 == 0):
            mutiples.append(i) #Appends all the mutiples of 5 to the empty list [mutiples]
    print("Sum of mutiples= %d" %sum(mutiples)) #Outputs the sum of all the mutiples of 3 and 5 
    print(mutiples)
    
#9. Write a function called show_stars(rows). If rows is 5, it should print the following:
rows = int #defining rows as a global variable

def show_stars(rows):
"""
This functions prints rows of stars if the number in the input function is greater than or equal to 5.
"""
    if rows >= 5: # Condition that only prints stars if the row number entered is greater than or equal to 5.
        print("*")
        print("**")
        print("***")
        print("****")
        print("*****")

#Question 10.
                    
limit= int #Assigning limit as any integer value that a user puts in
primes = [] #Initializing an empty list 

def PrimeNo(limit): #Describing a function named PrimeNo that takes one parameter (limit) inside.
"""
This function sums gives a list of all prime numbers between 0 and a given limit.
"""
    for possiblePrime in range(2, limit): # The range function begins from 2 because there are no prime numbers less than 2. The limit is set by the input the user keys in.
        isPrime = True  #Assigning is prime as a tag that is equated to TRUE unless it is changed.
            for num in range(2, possiblePrime): #Possible prime is every prime number that exists between 0 and limit
                if possiblePrime % num == 0: #This is a condition to remove all the non-prime numbers.
                    isPrime = False #Tag is changed to false if a non prime number is found

            if isPrime: #If IsPrime=True then the consecutive actions will be excecuted
                primes.append(possiblePrime) #Takes all possible prime numbers and appends to earlier empty list[primes].
                print(possiblePrime)#prints all prime numbers between 0 and limit
            print(number)#includes the limit to output of the function

