#question 1
def TowerOfHanoi(n,source,destination,auxilliary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1,source,auxilliary,destination)
    print("Move disk",n," from source",source,"to destination",destination)
    TowerOfHanoi(n-1,auxilliary,destination,source)

TowerOfHanoi(3,'A','C','B')    

    
#question 2
print("USING LOOPS")   #using loops
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input('Enter the size of pascals triangle: '))
for i in range(n):
	for j in range(n-i+1):
		print(end=" ")   #for spacing

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	   # for new line

print("USING RECURSSIONS")   #using recurssion
def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='')

    #first number is always 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
        
        #using Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)

#question3
a=int(input("enter 1st no.:"))
b=int(input("enter 2nd no.:"))
Quotient = a // b
Remainder = a % b

#a)
print(" Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#b)
if (Quotient == 0):
    print(" The quotient is zero")
if (Remainder == 0):
    print(" The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print(" All the values are non zero")
    
#c)
list = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(list)):
    if list[i] > 4:
        result.append(list[i])
print(f" Filtered out numbers that are greater than 4 are : {result}")

#d)
setresult = set(result)
print("Set:",setresult)

#e)
immutableSet = frozenset(setresult)   #frozen Set is used to make the set immutable
print("Immutable set:",immutableSet)

#f)
maxval=0        #max value from the set
for i in immutableSet:
    if i>maxval:
        maxval=i
print("The required max value is-",maxval)
print("The required hash value is-",hash(maxval))



#question 4
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def __del__(self):
        print("object destroyed")
        
p1=Student("Yashita",39)
print(p1.name)
print(p1.rollno)
del p1


#question 5
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

p1=Employee("Mehak",40000)
p2=Employee("Ashok",50000)
p3=Employee("Viren",60000)

#updating salary of Mehak to 70000
p1.salary=70000
print("The updated salary of Mehak is-",p1.salary)

#deleting the record of Viren
del p3
print("The record of Viren has been successfully deleted.")


#question 6
def anagram(word):        #here we use the concept of anagrams
    if len(word)==1:
        return [word];
    partial_words=anagram(word[1:])
    char=word[0]
    result=[]
    for perm in partial_words:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
    return result        


George_word=input("George,give a word-")
Possible_words=anagram(George_word)
Barbie_word=input("Barbie,Give a word-")
print("Possible Words-",Possible_words)      #anagrams of word entered by George 
print("If Barbie's word lies in the list,then their friendship is real.")

if Barbie_word in Possible_words:
    print("Friendship is real.")
else:
    print("Friendship is fake.")


        
	
