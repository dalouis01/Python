import random , string
alfabe = string.ascii_lowercase 
def fonksyon(kantite):
    mo_al = ""
    for i in range(kantite):
        mo_al += random.choice(alfabe) 
    return (mo_al)
print(fonksyon(int(input("Rantre kantite a "))))