atm_dic={'c1': 1000 ,'c2': 1000}
i=[1,2,3,4]
#print(sys.getsizeof(i))
#print(sys.getsizeof(atm_dic))
atm_dic['c1']-=50
print(atm_dic)
votes={}
i=0

voter={'n1': 1 , 'n2' : 2}
votes.update(voter)
n=input("enter")
if n == 'n1':
    i+=2
print(votes)
print(i)
votes['n1']=i
print(votes)
print(votes.keys())
print(votes.values())
print(votes)
if 2 in votes.values():
    print(votes.fromkeys('n2'))
    votes.pop("n1")
    print(votes)
    print( votes.__getitem__('n2'))
