#!/usr/bin/python3
from random import randrange
from math import ceil

total = 1000
play = True

print ("Vous vous installez a la roulette avec ", total, "$", sep="")

while play:
    mise = input("Combien souhaitez vous miser ? ")
    
    try:
        mise = int(mise)
        assert mise > 0 
        assert mise <= total
    except ValueError:
        print("Vous n'avez pas saisi un nombre")
        continue
    except AssertionError:
        print("La mise saisie est inferieure ou egale a 0 ou superieure a votre total")
        continue

    case = input("Sur quelle case souhaitez vous miser (0-49) ? ")

    try:
        case = int(case)
        assert case >= 0
        assert case < 50
    except ValueError:
        print("Vous n'avez pas saisi un nombre")
        continue
    except AssertionError:
        print("La case saisie est mauvaise")
        continue

    tirage = randrange(50)

    print ("Le numero gagnant est ", tirage, sep="")
    gain = 0

    if tirage == case:
    	gain = int(3 * mise)
    	print ("Bingo ! Vous remportez ", gain, " plus votre mise", sep="")
    elif tirage % 2 == case % 2:
    	gain = int(ceil(mise / 2))
    	print ("Meme couleur ! Vous remportez ", gain, " plus votre mise", sep="")

    if gain > 0:
    	total = int(total + gain)
    else:
    	total = int(total - mise)

    print ("Votre nouveau total est ", total, sep="")

    if total <= 0:
    	play = False
    	print("Partie terminee")
    



