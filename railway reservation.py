price_of_tcket=500
import time
lst=[]
for i in range(1,51):
    lst.append(i)
name=[]
for j in range(1,51):
    name.append(j)
age=[]
for k in range(1,51):
    age.append(k)
    count=0
while True:
    print("""railway reservation
            1.book ticket
            2.ticket info
            3.cancel ticket
            4.detail of ticket
            5. exit """)
    choice=int(input("enter your choice"))
    if choice==1:
        count+=1
        tck=int(input("enter the ticket number you want to book"))
        if lst[tck-1]== tck:
             nam=str(input("enter your name"))
             ag=int(input("enter your age"))
             lst.pop(tck-1)
             name.pop(tck-1)
             age.pop(tck-1)
             lst.insert(tck-1,'b')
             name.insert(tck-1,nam)
             age.insert(tck-1,ag)
             print("booked ticket")
             c=input("do u want to book more ticket?")
             if c=='y':
                 continue

             elif c=='n':
                pay=count*price_of_tcket
                print("pay amount of",pay)
                payed=int(input())
             if payed== pay:
                print("payment done")

             else:
                 print("not paid")

        else:
             print("ticket already booked")
    if choice == 3 :
        tck=int(input("enter the ticket number"))
        if lst[tck-1]==tck:
            print("ticket not booked")
            #sleep(5)
        else:
            lst.pop(tck-1)
            lst.insert(tck-1,tck)
            print("sucessfully cancelled")

    if choice == 4:
        tck = int(input("enter the ticket number"))
        if lst[tck-1]==tck:
            print("ticket not booked")

        else:
            print("your name is ",name[tck-1],"your age is",age[tck-1],"status of ticket",lst[tck-1])

    if choice== 5:
        print("thank u")
        break