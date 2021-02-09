fc_ticket=[]
sc_ticket=[]
ticket_cost_fc=250
ticket_cost_sc=150
count=0
name=[]
for i in range(1,10):
    fc_ticket.append(i)
for j in range(11,50):
    sc_ticket.append(j)
for k in range(1,50):
    name.append(k)
while True:
    print("""enter your choice
             1.book ticket
             2.delete ticket
             3.ticket info
             4.eixt""")
    choice=int(input('enter the choice:'))
    if choice==1:
        count+=1
        print("""enter the type of ticket
            1.first class(
            2.second class""")
        c=int(input('enter the type of ticket'))
        if c==1 :
            fc_tick=int(input('enter the ticket from 1-10'))
            nam=input('enter your name')
            if fc_tick <=10:
                if fc_ticket[fc_tick-1]==fc_tick:
                    fc_ticket.pop(fc_tick-1)
                    name.pop(fc_tick-1)
                    fc_ticket.insert(fc_tick-1,'b')
                    print(fc_ticket[fc_tick-1])
                    name.insert(fc_tick-1,nam)

                    ans=input('you wish to continue?')
                    if ans =='y':
                        continue
                    elif ans=='n':
                        bill=ticket_cost_fc*count
                        print("make a payment of",bill)
                        am=int(input())
                        if am == bill:
                            print("sucessfully booked",count,'tickets by',name[fc_tick-1])
                else:
                    print("ticket already booked")
       # else:
        #    print("full")
        if c==2 :
                sc_tick = int(input('enter the ticket from 11-50'))
                nam1 = input('enter your name')
                if sc_tick in range(11,50):
                    if sc_ticket[sc_tick-1]==sc_tick:
                        sc_ticket.pop(sc_tick-1)
                        name.pop(sc_tick-1)
                        sc_ticket.insert(sc_tick-1,fc_tick)
                        name.insert(sc_tick-1,nam1)
                        ans = input('you wish to continue?')
                        if ans == 'y':
                            continue
                        elif ans == 'n':
                            bill = ticket_cost_sc * count
                            print("make a payment of", bill)
                            am = int(input())
                            if am == bill:
                             print("sucessfully booked", count, 'tickets by', name[sc_tick - 1])
        else:
            print('second class is full')
    if choice == 2:
        de=int(input('enter the tick no to be deleted'))
        if de in range(1,10):
            fc_ticket.pop(de-1)
            fc_ticket.insert(de-1,de)
            print('sucessfully del')
        elif de in range(11,50):
            sc_ticket.pop(de-1)
            sc_ticket.insert(de-1,de)
            print('sucessfully del')
    if choice == 3:
        tic=int(input('enter the tick no to be deleted'))
        print("ticket booked by",name[tic-1],"no of ticket",count)
    if choice == 4:
        break
