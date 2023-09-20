print("enter two numbers");      # for taking input from user
num1=int (input());
num2=int (input());               
print("\n  1- addition ,\n  2-subtraction,\n  3-multiplication,\n  4-division"); #print operation choice for user
print("enter choice");                       #print choice statement
ch=int(input())                              #store input value in ch
if ch==1:  
   print("addition is",(num1+num2));         #print addition of two no 
elif ch==2:  
   print("subtraction is",(num1-num2));       #print subtraction of two no 
elif ch==3:  
   print("multiplication is",(num1*num2));    #print multiplication of two no 
elif ch==4: 
   print("division is",(num1/num2));          #print division of two no 
else:  
   print("invalid choice");                   #print if user give wrong choice
   
