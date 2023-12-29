#Formatting output with using '%' and '{}'

#1st Approch
# name="Abhishek"
# age=30
# sal=50000.50

name,age,sal="Abhishek",30,50000.50
# print(name,age,sal)

#2nd Approch
# print("Name is:",name)   #Name is: Abhishek
# print("Age is:",age)     #Age is: 30
# print("Sal is:",sal)     #Sal is: 50000.5

#3rd Approch
#print("Name is:%s Age is:%d Sal is:%g" %(name,age,sal))   #Name is:Abhishek Age is:30 Sal is:50000.5

#4th Approch
print("Name is:{} Age is:{} Sal is:{}" .format(name,age,sal))
print("Age is:{} Name is:{}  Sal is:{}" .format(age,name,sal))