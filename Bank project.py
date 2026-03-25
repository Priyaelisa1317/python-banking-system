print('='*47)
s="WELCOME TO AJAY BANK"
print(s.center(47,'-'))
print('*'*47)
print('=<< 1. Open a new account                   >>=')
print('=<< 2. Withdraw Money                       >>=')
print('=<< 3. Deposit Money                        >>=')
print('=<< 4. Check Customer Balnace               >>=')
print('=<< 5. Exit/Quit                            >>=')
print('*'*47)


k=1
r=1
while k==r:
     a=input("select any one number from the above menu:")
     print('choice number',a,'is selected by the customer')
     if a=='1':
         
         w=int(input('enter your aadhar number: '))
         x=input('Give your full name: ')
         y=int(input('enter a 4-digit pin as your wish:'))
         z=int(input('Enter the initial amount to deposit:')) 
         if z<500:
             print('minimum balance is low..\n account cannot be created')
         else:
             print('your account is created successfully')
     elif a=='2':
         f=int(input("enter your account number:"))
         bal=int(input("enter your withdarw amount:"))
         z-=bal
         
         
     elif a=='3':
         f=int(input("enter your account number:"))
         bal=int(input("enter your deposit amount:"))
         z+=bal
        
     
     elif a=='4':
         f=int(input("enter your account number:"))
         print(z)

         
     elif a=='5':
         t="Thank you for visiting our bank"
         print(t.center(47,'-'))
         k+=1
         
         
