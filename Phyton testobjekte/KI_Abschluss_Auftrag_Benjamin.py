import csv


def daten_einlesen(dateiname):
    features = []
    labels = []
    with open(dateiname) as datei:
        for zeile in csv.reader(datei):  # Jede Zeile
            features.append(zeile[:-1])  # Alle Spalten ausser der letzten
            labels.append(zeile[-1])  # Die letzte Spalte
    features = [[float(x) for x in zeile] for zeile in features]  # Sicherstellen, dass alles Zahlen sind
    return features, labels


features, labels = daten_einlesen("Rossinen Data.csv")
EPOCHEN = 20
LERNRATE = 0.01

w0 = 0.4
w1 = 0.2
w2 = 0.0
w3 = 0.3
w4 = 0.5
w5 = 0.2
w6 = 0.1
w7 = 0.4


for i in range(EPOCHEN):
    print(f"Epoche {i+1}:")

    richtig = 0
    falsch = 0

    for messwerte, label in zip(features, labels):

        x0 = 1
        x1 = messwerte[0]
        x2 = messwerte[1]
        x3 = messwerte[2]
        x4 = messwerte[3]
        x5 = messwerte[4]
        x6 = messwerte[5]
        x7 = messwerte[6]


        z = w0 * x0 + w1 * x1 + w2 * x2 + w3 * x3 + w4 * x4 + w5 * x5 + w6 * x6 + w7 * x7
        
        if z > 0:
            schaetzwert = 1
        else:
            schaetzwert = -1

        if label == "Kecimen":
            richtiger_wert = 1
        elif label == "Besni":
            richtiger_wert = -1
        else:
            raise ValueError(f'Unbekannter Wert: "{label}"')


        if schaetzwert == richtiger_wert:
            richtig += 1
        else:
            falsch += 1

        w0 += x0 * (richtiger_wert - schaetzwert) * LERNRATE
        w1 += x1 * (richtiger_wert - schaetzwert) * LERNRATE
        w2 += x2 * (richtiger_wert - schaetzwert) * LERNRATE
        w3 += x3 * (richtiger_wert - schaetzwert) * LERNRATE
        w4 += x4 * (richtiger_wert - schaetzwert) * LERNRATE
        w5 += x5 * (richtiger_wert - schaetzwert) * LERNRATE
        w6 += x6 * (richtiger_wert - schaetzwert) * LERNRATE
        w7 += x7 * (richtiger_wert - schaetzwert) * LERNRATE

    print(f"{richtig=}, {falsch=}")
    print(f"{w0=:.3}, {w1=:.3}, {w2=:.3}, {w3=:.3}, {w4=:.3}, {w5=:.3}, {w6=:.3}")

z = w0 * x0 + w1 * x1 + w2 * x2 + w3 * x3 + w4 * x4 + w5 * x5 + w6 * x6 + w7 * x7

testcountR = 0
testcountF = 0

#features, labels = daten_einlesen("Rossinen Data copy.csv")  #testen ob es funktioneret 

#print(f"{features=}")
#print(f"{labels=}")

for tmesswerte, tlabel in zip(features, labels):
    

    tx0 = 1
    tx1 = tmesswerte[0]
    tx2 = tmesswerte[1]
    tx3 = tmesswerte[2]
    tx4 = tmesswerte[3]
    tx5 = tmesswerte[4]
    tx6 = tmesswerte[5]
    tx7 = tmesswerte[6]

            
    z = w0 * tx0 + w1 * tx1 + w2 * tx2 + w3 * tx3 + w4 * tx4 + w5 * tx5 + w6 * tx6 + w7 * tx7
    
    print(z)
    
    if z > 0:
        schaetzwert = 1
            
    else:
        schaetzwert = -1

        
    if tlabel == "Kecimen":
        richtiger_wert = 1
    elif tlabel == "Besni":
        richtiger_wert = -1
        
        
    if schaetzwert == richtiger_wert:
        testcountR += 1
    else:
        testcountF += 1
            

print(f"{testcountF=}, {testcountR=}")
print(f"{w0=:.3}, {w1=:.3}, {w2=:.3}, {w3=:.3}, {w4=:.3}, {w5=:.3}, {w6=:.3}")
