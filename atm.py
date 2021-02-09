card_pass={'c1':1111,'c2':2222}
card_bal={'c1':10000,'c2':20000}
card_name={'c1':'xxx','c2':'yyy'}

while True:
      card=input("insert the card")
      if card in card_pass:
              print("verified welcome",card_name[card])
              print("""choose your option
                    1.withdraw
                    2.deposit
                    3.check balance""")
              choice=int(input('enter the choice '))
              if choice == 1:
                  pas = int(input("enter the password:"))
                  if pas in card_pass.values():
                      am=int(input("enter amount u want to withdraw"))
                      if am < card_bal[card]:
                          card_bal[card]-=am
                          print("remaining:",card_bal)
                      else:
                          print("no sufficient balance")
                  else:
                      print("wrong passwword")
              if choice == 2:
                  pas=int(input("enter the password:"))
                  if pas in card_pass.values():
                      amount=int(input("enter amount u want to deposit"))
                      card_bal[card]+=amount
                      print("remaining:", card_bal)
              if choice == 3:
                  pas =int(input("enter the password:"))
                  if pas in card_pass.values():
                      print(card_bal[card])
              if choice == 4:
                   break

      else:
          print("not a valid card")