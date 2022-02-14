# Créé par mathd, le 29/11/2021 en Python 3.7


##fruits = ["pomme", "orange", "poire", "fraise", "peche"]
##
##for fruits in fruits :
##    print(fruits)


##nb1 = input("entre le nombre 1: ")
##nb2 = input("entre le nombre 2: ")
##
###créer une fonction
##def sum(nombre1, nombre2) :
##    total = int(nombre1) + int(nombre2)
##    print(total)
##
##sum(nb1, nb2)


prenom = input("Entre votre prénom :")
nom = input("Entre votre nom :")
age = int(input("Entre votre age :"))
print("--------------------------------------------------------------")
print("Bienvenue", prenom, nom)

ticket = 0

if age >= 18 :
    ticket = 9

elif age > 12 :
    ticket = 8

elif age <= 12 :
    ticket = 7


print("Le prix du ticket est de ", int(ticket), "€.")
print("--------------------------------------------------------------")

shop = int(input("Voulez-vous acheter quelque chose ? :\n 1 : oui\n 2 : non"))

wallet = int(input("Combien d'euros possedez-vous ?"))
tempWallet = wallet
wallet = wallet - ticket


while shop == 1 :

   if shop ==1 :

    buy = int(input("Tapez 1 pour acheter un Popcorn Small (3€)\n Tapez 2 pour acheter un Popcorn Medium (4€)\n Tapez 3 pour acheter un Popcorn XL (5€)\n Tapez 4 pour acheter une boisson (3€)"))
    totBuy = 0

   if buy == 1 :
    print("***--------------------------------------------------------------***")
    print("***+1 Popcorn Small, voulez-vous acheter autre chose ?***")
    print("***--------------------------------------------------------------***")
    wallet = wallet - 3
    totBuy = totBuy + 3

   elif buy == 2 :
    print("***--------------------------------------------------------------***")
    print("***+1 Popcorn Medium, voulez-vous acheter autre chose ?***")
    print("***--------------------------------------------------------------***")
    wallet = wallet - 4
    totBuy = totBuy + 4

   elif buy == 3 :
     wallet = wallet - 5
     totBuy = totBuy + 5
     print("***--------------------------------------------------------------***")
     print("***+1 Popcorn XL, voulez-vous acheter autre chose ?***")
     print("***--------------------------------------------------------------***")

   elif buy == 4 :
     wallet -= 3
     totBuy = totBuy + 3
     print("***--------------------------------------------------------------***")
     print("***+1 Boisson, voulez-vous acheter autre chose ?***")
     print("***--------------------------------------------------------------***")

   elif buy == 5 :
     shop = 2


if shop == 2 :
 if age < 18 :
   red =  totBuy/100*10
   print("--------------------------------------------------------------")
   total = print("Votre total à payer est de ", tempWallet - ticket - totBuy,"€")
   print("--------------------------------------------------------------")

 else :
   red = 0
   print("--------------------------------------------------------------")
   total = print("Votre total à payer est de ", tempWallet - ticket - totBuy,"€")
   print("--------------------------------------------------------------")






