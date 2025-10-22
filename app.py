print("lets start")


project = input(" do you want play ?")

if project != "yes":

    quit()

win = 0
 


print("lets start again")

name = input("what is the cpu ?")

if name == "central processing unit":
   print("correct")
   win += 1
    
else:
   print("incorrect")
    
    



vlan = input("cosa sono le vlan")
if vlan == "virtual local area network":
   print("correct")
   win += 1
    
else:
    print("incorrect")
     
    

vpn = input("cosa sono le vpn")    
if vpn =="virtual private network":
   print("correct")
   win += 1
    
else:
    print("incorrect")
     


print("ha segnato " + str(win)+ " corretti")

 