import csv


SPRACHEN_IM_DATENSATZ = ["D", "F"]  # Für eine höhere Challenge andere Sprachen verwenden (z.B. "I" vs. "E"), oder drei


def bestimme_sprache(text):
    # Hier kommt Ihr Code!
    if "und" in text or "oder" in text or "ö" in text or "ä" in text or "ü" in text:
        return "D" 
    else:
        return "F"

def daten_einlesen(dateiname):
    with open(dateiname) as datei:
        return [(text, sprache) for (text, sprache) in csv.reader(datei) if sprache in SPRACHEN_IM_DATENSATZ]


texts, labels = zip(*daten_einlesen("sprachunterscheidung.csv"))
korrekt_identifiziert = {sprache: 0 for sprache in SPRACHEN_IM_DATENSATZ}
fehlerhaft_identifiziert = {sprache: 0 for sprache in SPRACHEN_IM_DATENSATZ}
verpasst = {sprache: 0 for sprache in SPRACHEN_IM_DATENSATZ}

for text, echte_sprache in zip(texts, labels):
    vermutete_sprache = bestimme_sprache(text)
    if vermutete_sprache == echte_sprache:
        korrekt_identifiziert[echte_sprache] += 1
    else:
        fehlerhaft_identifiziert[vermutete_sprache] += 1
        verpasst[echte_sprache] += 1

try:
    print(f"Trefferquote: {sum(korrekt_identifiziert.values()) / len(texts):.1%}")
    print("Behauptete Verteilung:")
    for sprache in SPRACHEN_IM_DATENSATZ:
        print(f"{sprache:2}: {(korrekt_identifiziert[sprache] + fehlerhaft_identifiziert[sprache])/len(texts):.1%}")
    print("Tatsächliche Verteilung:")
    for sprache in SPRACHEN_IM_DATENSATZ:
        print(f"{sprache:2}: {(korrekt_identifiziert[sprache] + verpasst[sprache])/len(texts):.1%}")
    print("Korrektheitsquote unter Behauptungen:")
    for sprache in SPRACHEN_IM_DATENSATZ:
        print(f"{sprache:2}: {korrekt_identifiziert[sprache] 
                              / (korrekt_identifiziert[sprache]+fehlerhaft_identifiziert[sprache]):.1%}")
    print("Gefunden:")
    for sprache in SPRACHEN_IM_DATENSATZ:
        print(f"{sprache:2}: {korrekt_identifiziert[sprache] 
                              / (korrekt_identifiziert[sprache]+verpasst[sprache]):.1%}")
43
except ZeroDivisionError:
    print("Manche Sprachen werden überhaupt nicht behauptet... Den Filter sollte man vielleicht überdenken.")
