import sys

n  = int(input("Enter the number of students :"))

i = 0

student_dict = {}

  
def calculate_avg(nm,n):
    if nm in student_dict.keys():
        sum=0
        for x in range(0,3):
            sum = sum + student_dict[nm][x]
            x += 1
          
        avg = sum/n
        return avg
    else :
        return "error"             
           
while i<n:
  name=input("enter name:")
  phy = float(input("Physics marks:"))
  math = float(input("Maths marks:"))
  chem =  float(input("Chemistry marks:"))
  
  student_dict[name] =[phy, math, chem ]
  i += 1

  
  
std = input("Enter the student name you want:")
print (student_dict)

avg_marks = calculate_avg(std,n)

  
print ("the value is :" + str(avg_marks))
  

