#queston1
s=input("enter a statement:") #s is for input string
print(s)
print(len(s)) #length of the string
print(s[::-1]) #reverse order
new_string=s[10:26]
print(new_string)
print(s.replace("a case sensitive","object oriented"))
print(s.find('a')) #index value of a
print(s.replace(" ","")) #remove spaces


#question2
name="Yashita Bansal"
SID=21103056
dept_name="CSE"
CGPA=10.0
print("Hey,%s Here!" %(name))
print("My SID is %d" %(SID))
print("I am from %s department and my CGPA is %f"%(dept_name,CGPA))


#question3
a=56
b=10
print("a&b:",a&b)
print("a|b:",a|b)
print("a^b:",a^b)
print("a<<2:",a<<2)
print("b<<2:",b<<2)
print("a>>2:",a>>2)
print("b>>4:",b>>4)


#question4
a=input("enter 1st no.")
b=input("enter 2nd no.")
c=input("enter 3rd no.")
if a>b:
    if a>c:
         print("largest no. is:",a)
    else:
        print("largest no. is:",c)
else:
    print("largest no. is:",b)


#question5
s=input("enter a sentence:")
if "name" in s:
    print("yes")
else:
    print("no")


#question6
a=int(input("enter 1st side of a triangle:"))
b=int(input("enter 2nd side of a triangle:"))
c=int(input("enter 3rd side of a triangle:"))
if a>b+c or b>a+c or c>a+b:
    print("no")
else:
    print("yes")
    



        
        

    
                
