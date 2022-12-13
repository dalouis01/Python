import re
def fonk_ini(mo):
    mo = re.split('-+| +',mo)
    inisyal = [i[0] for i in mo] 
    return "".join(inisyal)
print(fonk_ini(input("Rantre non ou bezwen inisyal li a ")))