#Question 1
s=input("enter a string:")
s=s.lower()
a=s.split(" ")
d={}  #initialising a dictionary
b=[]  #initialising a list
if len(a)==1:  #to check if the string is a word or a sentence 
    c=list(s)  #to get each character of the word
    for i in c:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print("no. of occurences of each character in word is:\n",d)
else:
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print("no. of occurences of each word in string is:\n",d)



#Question 2
month=int(input("Give month[1-12] in the form 2 not 02-"))


if(month in[1,3,5,7,8,10,12]):     #month having 31 days
    day=int(input("Give day[1-31]-"))
    if(1<=day<=31):
        year=int(input("Give year[1800-2025]-"))
        if(1800<=year<=2025):
            print("Date-",day,"/",month,"/",year)
            if(month==12 and day==31):
                print("Next Date-","1/1/",year+1)
            elif(day==31):
                print("Next Date-","1/",month+1,"/",year)
            else:
                print("Next Date-",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
         print("invalid date") 
elif(month in[4,6,9,11]):          #month having 30 days
    day=int(input("Give day-"))
    if(1<=day<=30):
        year=int(input("Give year-"))
        if(1800<=year<=2025):
            print("Date-",day,"/",month,"/",year)
            if(day==30):
                print("Next Date-","1/",month+1,"/",year)
            else:
                print("Next Date-",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
         print("invalid date")
elif(month==2):                   #month is february
    year=int(input("Give year-"))
    if(1800<=year<=2025):
        day=int(input("Give day-"))
        if(year%4==0):            #Its a leap year
            if(1<=day<=29):
                print("Date-",day,"/",month,"/",year)
                if(day==29):
                    print("Next Date-","1/",month+1,"/",year)
                else:
                    print("Next Date-",day+1,"/",month,"/",year)              
            else:
                print("invalid day")
        else:
            if(1<=day<=28):
                print("Date-",day,"/",month,"/",year)
                if(day==28):      
                    print("Next Date-","1/",month+1,"/",year)
                else:
                    print("Next Date-",day+1,"/",month,"/",year)       
            else:
                print("invalid day")     
    else:
        print("invalid year")
else:
    print("invalid month")



#Question 3    
input_string=input("Enter elements of a list separated by space:")
list=input_string.split()
print('list:',list)
for i in range(len(list)):
    list[i]=int(list[i])
    list[i]=(list[i],list[i]**2)
print(list)    



#Question 4
def input_grade():
    grade = int(input("Enter Grade : "))
    # check if the grade point meets the conditions
    if grade>10 or grade<4:
        print("Invalid grade! Try Again")
        grade = input_grade()
    return grade
grade=input_grade()
if(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")




#Question 5
Word="ABCDEFGHIJK"
counter=1    #counter tells the row no. and the alphabets should decrease after every row
while(counter<7):
    print(" "*(counter-1),Word[0:11-((counter-1)*2)])    #leaving gaps equal to (count-1)
    counter=counter+1



#Question 6
sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}

while True:
    choice = input("Do you want to enter another student entry(Y or N):").upper()
    if choice == 'Y':
        sid = int(input("Enter SID(Donot enter same SID): "))
        name = input("Enter Name: ")
        students[sid] = name
    elif choice == 'N':
        break
    else:
        print('Invalid input!')

print(students)   #print the dictionary
print({k:v for k,v in sorted(students.items(), key= lambda x:x[1])})   #sort according to the names
print({k:v for k,v in sorted(students.items())})                       #sort according to the SIDs
while True:
    sid = int(input("Search Name with SID: "))  #search a student by their SID
    if sid in students:
        break
    else:
         print("Invalid SID,Try again!")        #in case u entered wrong SID
print(students[sid])

   

#Question 7
first_term=int(input("Give a number-"))
second_term=int(input("Give a number-"))

series=[first_term,second_term]
n="y"       #now it will keep on printing the sequence till you say y and to stop it say n
while(n=="y"):
    series.append(series[len(series)-1]+series[len(series)-2])
    print(series)
    n=input("Give y to continue and n to stop printing the series further-").lower()
print(series)
sum=0
for i in series:   #average of fibonacci series
    sum=sum+i
print("Average of the sequence-")
print(sum/len(series))




#question 8
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

#(a)
required_Set=Set1^Set2         #in Set1 and Set2 but not both.
print(required_Set)
#(b)
required_Set=Set1^(Set2^Set3)  #in only one of the three sets Set1,Set2 and Set3.
print(required_Set)
#(c)
required_Set=(Set1&Set2)|(Set2&Set3)|(Set1&Set3)  #exactly two of the sets Set1, Set2 and Set3
print(required_Set)
#(d)
new_Set={1,2,3,4,5,6,7,8,9,10} #all integers in the range 1 to 10 that are not in Set1.
required_Set=new_Set-Set1
print(required_Set)
#(e)
required_Set=new_Set-(Set1|Set2|Set3) #all integers in the range 1 to 10 that are not in Set1,Set2 and Set3
print(required_Set)




        
    

