voter_id=[1,2,3,4,5]
no=len(voter_id)
nominees={'hr':1,'hrr':2}
nominees_cunt={}
count1=0
count2=0
def getkey(val):
    for key ,value in nominees.items():
        if val==value :
            return key
    return 'not exit'
while True:
    if voter_id == []:
        keym=max(nominees_cunt,key=nominees_cunt.get)
        v=list(nominees_cunt.values())
        per=(max(v)/no)*100
        print(keym,'own by',per)
        break
    else:
        voter=int(input('enter u r id'))
        if voter in voter_id:
            print('valid voter')
            voter_id.remove(voter)
            print(nominees)
            nom=input('enter the nominee')
            if nom in nominees.keys():
                if nominees[nom]==1:
                    count1+=1
                    nominees_cunt[nom]=count1
                elif nominees[nom]==2:
                    count2+=1
                    nominees_cunt[nom]=count2
            elif int(nom) in nominees.values():
                    if int(nom)==1:
                        count1+=1
                        key=getkey(int(nom))
                        nominees_cunt[key]=count1
                    elif int(nom)==2:
                        count2+=1
                        key = getkey(int(nom))
                        nominees_cunt[key] = count1


            else:
               print('not valid')