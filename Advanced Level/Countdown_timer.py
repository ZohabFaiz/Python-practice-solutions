import time #importing time

def countdown_timer(seconds): #creating a function
    while seconds > 0 :
        minutes=seconds//60                      #taking the ceil value for minutes
        secs=seconds % 60                        #taking the modulo operator
        timer= f'{minutes:02d}:{secs:02d}'       #passing the time string minutes and seconds to timer
        print(timer,end='\r')                    # end = '\r' updates the value or rewite at same place instead of changing the line 
        time.sleep(1)                            #timer is sleeping or at pause for 1 sec
        seconds-=1 
        

    print('⏰ Times Up!!')    



try:                 #prevents the code from crashing if user gives any input other than integer
 

 while True:        #keeps the while loop running until user gives correct input values i.e integer

        user_input=input('Enter your countdown timer in seconds: ')  #takes input from user




        if user_input.isdigit():       #checks if the input is integer or not
         countdown_timer(int(user_input))   #passes the integer input value to countdown function
         break                             #breaks the if condition

        else:
           print('enter a valid time! ')

           
except ValueError:                             #prevents valueError crash
                 print('enter a valid value')






 # if you dont want to have a loop for taking inputs after a wrong value use this code below and comment out the above try: part


''' # remove '' from the start and end of the line 46 and line 71
try:                 
 

        

 user_input=input('Enter your countdown timer in seconds: ')  




 if user_input.isdigit():       
      countdown_timer(int(user_input))   
                      
 else:
           print('enter a valid time! ')

           
           
except ValueError:                             
                 print('enter a valid value')



   
'''