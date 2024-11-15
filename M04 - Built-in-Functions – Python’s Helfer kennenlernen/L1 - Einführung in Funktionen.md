## Was sind Funktionen?

Eine Funktion ist ein blockstrukturierter Codeabschnitt, der eine spezifische Aufgabe ausführt. Funktionen helfen dabei, wiederholte Aufgaben zu kapseln und den Code modular zu gestalten.

### Aufbau einer Funktion
Eine Funktion in Python wird mit dem Schlüsselwort `def` definiert:

```python
def name_der_funktion(parameter1, parameter2):
    # Codeblock
    return ergebnis
```

**Beispiel einer einfachen Funktion:**
```python
def addiere_zahlen(a, b):
    return a + b

# Verwendung der Funktion
ergebnis = addiere_zahlen(3, 5)
print(ergebnis)  # Ausgabe: 8
```

### Vorteile von Funktionen
1. **Wiederverwendbarkeit**: Funktionen können mehrfach aufgerufen werden.
2. **Klarheit**: Funktionen machen den Code besser lesbar.
3. **Modularität**: Große Programme können in kleinere, handhabbare Teile zerlegt werden.

## Überblick über Standardfunktionen in Python

Python bietet eine Vielzahl von eingebauten Funktionen, die sofort genutzt werden können. Hier sind einige der wichtigsten Standardfunktionen:

### 1. `print()`
Die `print()`-Funktion gibt Daten in der Konsole aus.
```python
print("Hallo, Welt!")  # Ausgabe: Hallo, Welt!
```

### 2. `len()`
Die `len()`-Funktion gibt die Länge (Anzahl der Elemente) einer Sequenz oder eines Objekts zurück.
```python
wort = "Python"
print(len(wort))  # Ausgabe: 6
```

### 3. `type()`
Die `type()`-Funktion gibt den Datentyp eines Objekts zurück.
```python
zahl = 42
print(type(zahl))  # Ausgabe: <class 'int'>
```

### 4. `range()`
Die `range()`-Funktion wird verwendet, um Zahlenfolgen zu erstellen.
```python
for i in range(5):
    print(i)  # Ausgabe: 0, 1, 2, 3, 4
```

### 5. `input()`
Die `input()`-Funktion liest Benutzereingaben von der Konsole.
```python
name = input("Wie heißt du? ")
print(f"Hallo, {name}!")
```

### 6. `max()` und `min()`
Mit `max()` und `min()` können das Maximum und Minimum einer Sequenz ermittelt werden.
```python
zahlen = [3, 7, 1, 9]
print(max(zahlen))  # Ausgabe: 9
print(min(zahlen))  # Ausgabe: 1
```

### 7. `sum()`
Die `sum()`-Funktion summiert alle Elemente einer Liste.
```python
zahlen = [1, 2, 3, 4]
print(sum(zahlen))  # Ausgabe: 10
```

### 8. `sorted()`
Die `sorted()`-Funktion gibt eine sortierte Version einer Liste zurück.
```python
zahlen = [4, 2, 8, 1]
print(sorted(zahlen))  # Ausgabe: [1, 2, 4, 8]
```

### 9. `help()`
Mit `help()` können Sie sich Informationen über Funktionen oder Module anzeigen lassen.
```python
help(print)
```