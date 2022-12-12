def fonksyon(mo):   
    rmo = ""
    for i in range(len(mo)-1,-1,-1):
        rmo += mo[i]
    return(rmo)
mo = input("Rantre mo a ")
print(fonksyon(mo))
