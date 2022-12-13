
def fonks_deskryp(mo) :
    repons = []
    mo = mo.split("-")
    for i in range(len(mo)):
        repons.append(chr(65+int(mo[i])))
    return "".join(repons)
print(fonks_deskryp("0-11-14"))
    
