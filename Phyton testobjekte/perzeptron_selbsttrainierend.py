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


features, labels = daten_einlesen("iris_midi.csv")
EPOCHEN = 10
LERNRATE = 0.01

# Zufällige Startgewichte:
w0 = 0.4
w1 = 0.2
w2 = 0.0
w3 = 0.0
w4 = 0.0


for i in range(EPOCHEN):
    print(f"Epoche {i+1}:")

    # Statistik für diese Epoche
    richtig = 0
    falsch = 0

    # Wir trainieren einmal über das gesamte Datenset:
    for messwerte, label in zip(features, labels):

        x0 = 1
        x1 = messwerte[0]
        x2 = messwerte[1]
        x3 = messwerte[2]
        x4 = messwerte[3]

        # Wir klassifizieren anhand der Perzeptron-Formel und den bisher besten Gewichten
        z = w0 * x0 + w1 * x1 + w2 * x2 + w3 * x3 + w4 + x4
        if z > 0:
            schaetzwert = 1
        else:
            schaetzwert = -1

        # Wir weisen den möglichen Werten Zahlen zu, damit wir nachher damit rechnen können.
        if label == "Iris-virginica":
            richtiger_wert = 1
        elif label == "Iris-setosa":
            richtiger_wert = -1
        else:
            # Wir geben hier einen Fehler aus, da wir nur diese beiden Arten berücksichtigt haben.
            raise ValueError(f'Unbekannter Wert: "{label}"')

        # Für die Statistik:
        if schaetzwert == richtiger_wert:
            richtig += 1
        else:
            falsch += 1

        # Wir passen die Gewichte an:
        w0 += x0 * (richtiger_wert - schaetzwert) * LERNRATE
        w1 += x1 * (richtiger_wert - schaetzwert) * LERNRATE
        w2 += x2 * (richtiger_wert - schaetzwert) * LERNRATE
        w3 += x3 * (richtiger_wert - schaetzwert) * LERNRATE
        w4 += x4 * (richtiger_wert - schaetzwert) * LERNRATE

    print(f"{richtig=}, {falsch=}")
    print(f"{w0=:.3}, {w1=:.3}, {w2=:.3}, {w3=:.3}, {w4=:.3}")
