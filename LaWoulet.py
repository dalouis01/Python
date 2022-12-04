# Fonksyon ki retounen yon nonb aleyatwa nan yon entèval
from random import randrange
nonb_odinate = randrange(0 , 500) # entèval [0 - 500]
# print(nonb_odinate)
print("           ===== Byenvini Nan Jwet La Woulèt la ===== \n")
print(" Chwazi yon nonb ant 0 ak 499 , si li egal ak pa odinate a wap genyen \n")
chans = 5 # Kantite chans jwè a genyen
while chans > 0 :
    print("Ou gen ",chans,"chans \n") 
    nonb_chwazi = int(input("Ki nonb ou chwazi itilizatè? ")) 
    if nonb_chwazi > nonb_odinate :
        print("\nNonb ou chwazi a pi gran ")
        chans -= 1
    elif nonb_chwazi < nonb_odinate :
        print("\nNonb ou chwazi a pi piti ")
        chans -= 1
    elif nonb_chwazi == nonb_odinate :
        print("\n Ou Genyen !!!!")
        break
if chans == 0 :
    print("\nOu pèdi")