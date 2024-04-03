# Die Klasse 'Fahrzeug' wird um ein Attribut 'Geschwindigkeit' erweitert
class Fahrzeug:
    # Hier soll das Attribut 'geschwindigkeit' standardmäßig auf den
    # Wert 0 gesetzt werden,
    # da am Anfang jedes Fahrzeug zunächst still steht.
    def __init__(self, antrieb, anzahl_räder=0, farbe="schwarz", geschwindigkeit=0): # ....
        self.anzahl_räder = anzahl_räder
        self.farbe = farbe
        self.antrieb = antrieb
        self.geschwindigkeit = geschwindigkeit
        #....

    def beschleunigen(self):
        self.geschwindigkeit += 1
        ausgabe = "Ich bin ein Fahrzeug mit Anzahl an Rädern: "
        ausgabe += str(self.anzahl_räder)
        ausgabe += ", Farbe: " + self.farbe
        ausgabe += " und Antrieb: "
        ausgabe += self.antrieb
        ausgabe += " und ich beschleunige jetzt."
        ausgabe += "\n"
        ausgabe += "Meine neue Geschwindigkeit ist: "
        ausgabe += str(self.geschwindigkeit) 
        print(ausgabe)

    def bremsen(self):
        self.geschwindigkeit += -1
        ausgabe = "Ich bin ein Fahrzeug mit Anzahl an Rädern: "
        ausgabe += str(self.anzahl_räder)
        ausgabe += ", Farbe: " + self.farbe
        ausgabe += " und Antrieb: "
        ausgabe += self.antrieb
        ausgabe += " und ich beschleunige jetzt."
        ausgabe += "\n"
        ausgabe += "Meine neue Geschwindigkeit ist: "
        ausgabe += str(self.geschwindigkeit) 
        print(ausgabe)
        
    

# Testen Sie Ihre Implementierung
motorrad = Fahrzeug("Benzin", 2, "grau", 80)
motorrad.beschleunigen()
motorrad.beschleunigen()
motorrad.bremsen()