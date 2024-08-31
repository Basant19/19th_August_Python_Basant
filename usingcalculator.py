from calculator import add ,sub, division , multiplication

while True:
    print ("press 1.Add ")
    print ("press 2.sub ")
    print ("press 3.multiplication ")
    print ("press 4.division ")
    print ("press 5.exist ")

    choice=int ( input ( " Enter your choice : "))

    if choice in range (1,5):
        num1= int ( input ( " Enter first number : "))
        num2= int ( input ( " Enter second number : "))
        print (num1)
        print (num2)
        if choice == 1:
            
            print (add(num1,num2))
        elif choice ==2:
            print (sub (num1,num2))    
        elif choice == 3:
            print (multiplication (num1,num2))

        elif choice == 4:
            print (division (num1,num2))
    else:
        if choice == 5:
            print ("bye")
            break     
        else:
            print (" Invalid Choice")
          
    




