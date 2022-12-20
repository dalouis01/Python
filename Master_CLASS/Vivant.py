
class Vivan:
    def __init__(self,pye,men,non,laj) -> None:
        self.pye = pye
        self.men = men
        self.non = non
        self.laj = laj
            
daniel = Vivan(2,2,"Louis",70)  
ricky = Vivan(2,2,"Jean",50)

class Poul(Vivan):
    def __init__(self,pat,non,laj) -> None:
        self.pat = pat
        self.non = non
        self.laj = laj

poul_peyi = Poul(2,"kirikou",2)
