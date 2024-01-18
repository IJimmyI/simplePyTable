

def tabelle_erstellen(spalten, spaltenbreite, zeilen, zeilenhoehe):
    # ERSTELLT DIE OBERE lINIE
    obere_linie = '╔' + '╦'.join(['═' * spaltenbreite for _ in range(spalten)]) + '╗'

    # ERSTELLT ZEILEN/ZEILENINHALTE UND TRENNLINIE
    zeilen_linie = []
    for _ in range(zeilen):
        # ERSTELLT ZEILE MIT ZEILENHÖHE
        for _ in range(zeilenhoehe):
            zeilen_inhalt = '║' + '║'.join([' ' * spaltenbreite for _ in range(spalten)]) + '║'
            zeilen_linie.append(zeilen_inhalt)

        # ERSTELLT DIE TRENNLINIE NACH JEDER ZEILE
        zeilen_linie.append('╠' + '╬'.join(['═' * spaltenbreite for _ in range(spalten)]) + '╣')

    # ENTFERNT DIE LETZTE ÜBERSCHÜSSIGE TRENNLINIE
    zeilen_linie.pop()

    # FÜGT UNTERE LINIE AN
    untere_linie = '╚' + '╩'.join(['═' * spaltenbreite for _ in range(spalten)]) + '╝'

    # ERSTELLEN DER PRINTAUSGABE
    print(f'print("{obere_linie}")')
    for linie in zeilen_linie:
        print(f'print("{linie}")')
    print(f'print("{untere_linie}")')

# EINGABE DER WERTE
spalten = int(input("Spaltenanzahl: "))
spaltenbreite = int(input("Spaltenbreite: "))
zeilen = int(input("Zeilenanzahl: "))
zeilenhoehe = int(input("Zeilenhöhe: "))

# AUSFÜHRUNG DER FUNKTION tabelle_erstellen 
tabelle_erstellen(spalten, spaltenbreite, zeilen, zeilenhoehe)
