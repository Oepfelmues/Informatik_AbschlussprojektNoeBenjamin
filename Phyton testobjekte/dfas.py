class Fahrzeug:
    """In dieser Zeichenkette steht eine Beschreibung des Objekts:
    Ein Fahrzeug hat eine Anzahl an Rädern, eine Farbe und
    eine Antriebstechnologie.
    Außerdem kann es beschleunigen und bremsen."""

    # Die Funktion mit dem Namen '__init__()' wird bei der Instanziierung
    # des Objektes aufgerufen, sie "initialisiert" also das Objekt.
    # Die __init__-Funktion hat als erste Variable immer
    # den 'self'-Zeiger.
    # 'self' stellt hierbei einfach das Objekt dar, welches
    # initialisiert wird.
    def __init__(self, antrieb, anzahl_räder=0, farbe="schwarz"):
        # Hierbei ist es möglich, Standardwerte zu übergeben
        # (siehe anzahl_räder und Farbe),
        # man muss dies aber nicht tun (siehe antrieb).
        # Wichtig ist, dass die Attribute mit Standardwerten immer
        # vor den Attributen ohne Standardwerten stehen.
        self.anzahl_räder = anzahl_räder
        self.farbe = farbe
        self.antrieb = antrieb

    # Methode zum Beschleunigen. Auch alle Methoden benötigen als
    # erstes Argument den 'self'-Zeiger.
    def beschleunigen(self):
        ausgabe = "Ich bin ein Fahrzeug mit Anzahl an Rädern: "
        ausgabe += str(self.anzahl_räder)
        ausgabe += ", Farbe: "
        ausgabe += self.farbe
        ausgabe += " und Antrieb: "
        ausgabe += self.antrieb
        ausgabe += " und ich beschleunige jetzt."
        print(ausgabe)

    # Methode zum Bremsen. Beachte den 'self'-Zeiger.
    def bremsen(self):
        ausgabe = "Ich bin ein Fahrzeug mit Anzahl an Rädern: "
        ausgabe += str(self.anzahl_räder)
        ausgabe += ", Farbe: "
        ausgabe += self.farbe
        ausgabe += " und Antrieb: "
        ausgabe += self.antrieb
        ausgabe += " und ich bremse jetzt."
        print(ausgabe)


# Hier werden nun Objekte dieser Klasse instanziiert.
auto = Fahrzeug("Diesel", 4, "rot")

# hier übergeben wir nur die Parameter,
# die kein Standardargument haben.
# Parameter mit einem Standardwert werden mit genau jenem
# Standardwert initialisiert. Dieses Auto hat also 0 Räder und
# ist schwarz (siehe oben).
schwarzes_auto_ohne_räder = Fahrzeug("Diesel")

sbahn = Fahrzeug("elektrisch", 64, "orange")
motorrad = Fahrzeug("Benzin", 2, "grau")
fz1 = Fahrzeug("elektrisch", farbe="pink")

# Rufe nun die Methoden der Objekte auf.
# Dabei ist die Syntax 'objektname'.'methode()'.
auto.beschleunigen()
motorrad.beschleunigen()
motorrad.bremsen()
sbahn.beschleunigen()
auto.bremsen()
sbahn.bremsen()

schwarzes_auto_ohne_räder.beschleunigen()
schwarzes_auto_ohne_räder.bremsen()