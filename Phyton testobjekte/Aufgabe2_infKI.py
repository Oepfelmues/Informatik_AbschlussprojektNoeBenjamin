from random import randint

class Charakter:
    def __init__(self, name='please enter name', maxHP=0, angr=50, vert=50):
        self.name = name
        self.maxHP = maxHP
        self.angr = angr
        self.vert = vert
        self.HP = maxHP 
    
    def get_angriffswert(self):
        self.angr

    def angriff(self, ziel):
        angriffswert = self.get_angriffswert()
        angriff = angriffswert - (angriffswert * (ziel.vert/100))
        if ziel.HP - angriff >= 0:
            ziel.HP += -angriff
        else:
            ziel.HP = 0
            print(ziel.name, ' ist gestorben ;(')
    
    def heilen(self):
        heilHP = 10
        if self.HP + heilHP <= self.maxHP:
            self.HP += heilHP
        else:
            self.HP = self.maxHP
            
    def status(self):
        print( 'Name:', str(self.name), ' HP:', self.HP)
        
    def __eq__(self, anderes_objekt):
        return self.name == anderes_objekt.name

class Schurkin(Charakter):
    def __init__(self, name='please enter name', maxHP=0, angr=50, vert=5, Krit=1):
        Charakter.__init__(self, name, maxHP, angr, vert)
        self.Krit = Krit

    def get_angriffswert(self):
        i= randint(1,10)
        if i >= 8:
            return self.angr * self.Krit
        else:
            return self.angr
    
    
      

    
char1 = Schurkin("KUEnigunde", maxHP=120, angr=145, vert=25, Krit=1.5)
char2 = Charakter("KUEnibert", maxHP=110, angr=90, vert=40)
char1.status()
char1.angriff(char2)  # KUEnigunde greift KUEnibert an!
char2.status()
char2.heilen()
char2.status()
# if char2.ist_tot():
#     print("FATALITY! KUEnigunde gewinnt!")

if char1 != char2:
    print("Identitätskrise!")
