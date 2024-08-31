from string_utils import lengthofstring , reversestring , captializestring 
def menu():
    while True:

        print ( "press 1 find length of string ")
        print ( "press 2 reverse of string " )
        print ( "press 3 captialize string  " )
        print ( "press 4 Exist ")

        choice = int (input ( "Enter your choice " ) )
        if choice in range (1,5):
            
            string= input ("Enter a string ")
        if choice == 1:

           print (lengthofstring(string))

        elif choice ==2:
            print (reversestring(string))

        elif choice ==3:
            print (captializestring(string)) 
        else :
          if choice == 4:
           
           print ("bye ")
           break
          else :                        
                 print ("Invalid choice  ")  

menu()                      
    
 
  
