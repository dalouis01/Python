import string
fonksyon_kriptaj = lambda mo: "-".join(str(string.ascii_uppercase.index(mo[i])) for i in range(len(mo)))
print(fonksyon_kriptaj(input("Rantre mo ou vle kripte a ").upper()))