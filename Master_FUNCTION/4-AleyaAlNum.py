import string , random
AlphaNum = string.ascii_lowercase + string.digits
def fonsksyon_alphanum(kantite):
    mo_al = ""
    inik = random.choice(AlphaNum)
    while(inik not in mo_al) and (kantite >0):
        mo_al += inik
        inik = random.choice(AlphaNum)
        while inik in mo_al:
            inik = random.choice(AlphaNum)
        kantite -= 1    
    return(mo_al)
print(fonsksyon_alphanum(int(input("Rantre Kantite a "))))