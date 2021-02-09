voter_id = [1, 2, 3, 4, 5]
nominees = {'hr1': 1, 'hr2': 2}
count1 = 0
count2 = 0
numvoter = len(voter_id)
while True:
    if voter_id == []:
        print("voting is over")
        if count1 > count2:
            per = (count1 / numvoter) * 100
            print(nominees['hr1'], "own by", per)
            break
        else:
            per = (count2 / numvoter) * 100
            print(nominees['hr2'], "own by", per)
            break
    else:
        voter_entered = int(input("enter the voter id"))
        if voter_entered in voter_id:
            print("valid voter to vote")
            voter_id.remove(voter_entered)
        else:
            print("not a valid voter")
       # for i in nominees:
        print(nominees)
        nominee_choosen =int(input('enter the nominee id you want to vote'))
        if nominee_choosen in nominees.values():
           if nominees == 1:
                count1 += 1
           elif nominee_choosen == 2:
                 count2 += 1
        else:
            print("not a valid nominee")
