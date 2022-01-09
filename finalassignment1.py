#assignment1
#by Harsh Sarwal, SID 21103063
#ques 1
print("pls enter your three numbers \n")
a=int(input("first number \n"))
b=int(input("second number \n"))
c=int(input("third number \n"))
print("the average of the three numbers",(a+b+c)/3)

#ques 2
print("hello taxpayer, using this program we will help you compute your income tax \n")
gi=float(input("what is your gross income \n"))
dep=int(input("pls enter the number of dependents \n"))
ti=(float(gi)-10000-(3000*int(dep)))
print("your taxable income is \n",ti)
print("and your tax is \n",int(ti)*0.20)

#ques 3
print("student details in the form of list \n")
a=int(input("enter your SID \n"))
b=str(input("what is your name \n"))
c=input("Enter your gender, Use Gender values: ‘F’, ‘M’, ‘U’ (For Unknown)\n")
d=input("course name \n")
e=float(input("CGPA \n"))
student=[a,b,c,d,e]
print(student)

#ques 4
print("sorting marks of five students")
a=int(input("marks of first student"))
b=int(input("marks of second student"))
c=int(input("marks of third student"))
d=int(input("marks of fouth student"))
e=int(input("marks of fifth student"))
marks=[a,b,c,d,e]
(marks).sort()
print('the sorted list is',marks)

#ques 5a
color=['Red','Green','White','Black','Pink','Yellow']
color.remove('Black')
print("color",color)

#ques 5b
color=['Red','Green','White','Black','Pink','Yellow']
color=color[:3] + ['Purple'] + color[3+2:]
print(color)
