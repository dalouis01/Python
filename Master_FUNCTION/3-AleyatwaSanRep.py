import random , string
alfabe = string.ascii_lowercase
def fonksyon_aleyatwa(kantite):
    mo_al= ""
    inik = random.choice(alfabe)
    while (inik not in mo_al) and (kantite > 0) :
        mo_al += inik
        inik = random.choice(alfabe)
        while inik in mo_al:
            inik = random.choice(alfabe)
        kantite -= 1
    return (mo_al)
print(fonksyon_aleyatwa(int(input("Rantre kantite a "))))

