import string
alph = "abcdefghijklmnopqrstuvwxyz"
lis = ["lis1","ki","pwal","tounen","slug"]
for let,idx in enumerate(lis):
    if let not in alph:
        res = lis[idx]= '-'
print(res)
#fonksyon_slug = lambda param : '-'.join(param)
#print(fonksyon_slug(lis))
