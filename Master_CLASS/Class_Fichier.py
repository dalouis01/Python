import os
class GestionFichier:
    
    def __init__(self,chemen) -> None:
        self.chemen = chemen
        
    def lifichye(self):
        fichye_a = open(self.chemen,'r')
        liy = fichye_a.readlines()
        for moso in liy :
            print(moso)
        fichye_a.close() 
        
    def ajoute(self):
        resep =[]
        fichye_a = open(self.chemen,'a')
        liy = input("Tape sa w vle ajoute nan fichye a")
        resep.append(liy)
        fichye_a.writelines(resep)
        fichye_a.close()
    
    def efasekontni(self):
        fichye_a = open(self.chemen,'r+')
        fichye_a.truncate(0)
        fichye_a.close()
    
    def efasefichye(self):
        adres = '/Users/Dany/Downloads'
        os.remove(adres)

test = GestionFichier('/Users/Dany/Downloads/text.txt')

