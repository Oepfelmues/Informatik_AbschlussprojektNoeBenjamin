# die Klasse 'Punkt' ist vorgegeben
class Punkt:

    # __init__-Funktion
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # gebe eine Repräsentation der Klasse als Zeichenkette zurück
    # diese Methode ist wie die'__str()__'-Methode
    def __repr__(self):
        return "Punkt[x=" + str(self.x) + ", y=" + str(self.y) + "]"


# die Elternklasse 'GeometrischeForm'
# class GeometrischeForm:
# Attribute
# ....
class GeometirscheForm(Punkt):
    def __init__(self,farbe='rot', strichdicke=1):
        self.farbe = farbe
        self.strichdicke = strichdicke
        

# __init__-Funktion
# ....

# die Kindklasse 'Quadrat' erbt von der Elternklasse 'GeometrischeForm'
# ....
class Quadrat(GeometirscheForm):
    def __init__(self, mittelpunkt= 'None', kantenlänge=1):
        self.mittelpunkt = mittelpunkt
        self.kantenlänge = kantenlänge
    

# die Kindklasse 'Kreis' erbt von der Elternklasse 'GeometrischeForm'
# ....
class Kreis(GeometirscheForm):
    def __init__(self, mittelpunkt= 'None', radius=1):
        self.mittelpunkt = mittelpunkt
        self.radius = radius
    

# erstelle Objekte der Klassen und gebe sie aus
quadrat = Quadrat("blau", 2, Punkt(3, 4), 5)
print(quadrat.__dict__)
kreis = Kreis("grün", 6, Punkt(7, 8), 9)
print(kreis.__dict__)