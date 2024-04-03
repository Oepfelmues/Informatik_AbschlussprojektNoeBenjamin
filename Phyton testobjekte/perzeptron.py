import csv


def daten_einlesen(dateiname):
    features = []
    labels = []
    with open(dateiname) as datei:
        for zeile in csv.reader(datei):  # Jede Zeile
            features.append(zeile[:-1])  # Alle Spalten ausser der letzten
            labels.append(zeile[-1])  # Die letzte Spalte
    return features, labels


features, labels = daten_einlesen("iris_mini.csv")


count_richtig = 0
count_falsch = 0
for i in range (1,10):
    for messwerte, label in zip (features, labels):
    #   print(f"Eine {label} mit den Messwerten {messwerte}.")

        #w0 = -7
        #w1 = 2
        #w2 = -1.46
        #w0 = 5
        n = 0.1
        dy = 1
        dw= (float(messwerte[0])-dy) (float(messwerte[1])) *n
        w1 = 1
        w2 = -4

        x0 = 1
        
        z = (dw * x0) + (w1 * float(messwerte[0])) + (w2 * float(messwerte[1]))
        print(z)
        print(label)
        if z > 0:
            print("Iris-setosa")
            if "Iris-setosa" == label:
                print("richtig")
                count_richtig += 1
            else: 
                print("falsch")
                count_falsch += 1
        else: 
            print("Iris-versicolor")
            if "Iris-versicolor" == label:
                print("richtig")
                count_richtig += 1
            else: 
                print("falsch")
                count_falsch += 1
                
    print("Richtig:", count_richtig)
    print("Falsch:", count_falsch)