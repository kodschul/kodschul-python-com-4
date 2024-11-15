## Funktionen definieren und aufrufen

Funktionen sind grundlegende Bausteine in Python, die dazu dienen, wiederverwendbaren und modularen Code zu schreiben. Eine Funktion wird definiert, indem das Schlüsselwort `def` verwendet wird, gefolgt vom Namen der Funktion und einer Klammer, die optionale Parameter enthalten kann.

### Syntax einer Funktion
```python
def funktionsname(parameter1, parameter2):
    # Funktionskörper
    return ergebnis
```

### Beispiel einer einfachen Funktion
```python
def begruessung():
    print("Hallo, willkommen zur Python-Schulung!")

# Funktion aufrufen
begruessung()
```

**Ausgabe:**
```
Hallo, willkommen zur Python-Schulung!
```

### Vorteile der Verwendung von Funktionen
- **Code-Wiederverwendbarkeit**: Funktionen können mehrfach aufgerufen werden, ohne den Code zu duplizieren.
- **Modularität**: Funktionen helfen dabei, Code in kleinere, leichter zu wartende Einheiten zu zerlegen.
- **Lesbarkeit**: Sie verbessern die Struktur und Lesbarkeit des Codes.

## Übergabe- und Rückgabewerte

### Parameter und Argumente
Funktionen können Parameter akzeptieren, die beim Aufruf der Funktion übergeben werden. Diese Parameter werden innerhalb der Funktion wie normale Variablen verwendet.

#### Beispiel mit Parametern
```python
def addiere(a, b):
    ergebnis = a + b
    print(f"Die Summe von {a} und {b} ist {ergebnis}")

# Argumente übergeben
addiere(3, 5)
```

**Ausgabe:**
```
Die Summe von 3 und 5 ist 8
```

### Rückgabewerte
Eine Funktion kann mit dem Schlüsselwort `return` einen Wert zurückgeben. Dieser Wert kann dann in anderen Teilen des Programms verwendet werden.

#### Beispiel mit Rückgabewerten
```python
def multipliziere(a, b):
    return a * b

ergebnis = multipliziere(4, 6)
print(f"Das Ergebnis der Multiplikation ist {ergebnis}")
```

**Ausgabe:**
```
Das Ergebnis der Multiplikation ist 24
```

### Standardwerte für Parameter
Funktionen können Standardwerte für Parameter definieren, die verwendet werden, wenn kein entsprechendes Argument übergeben wird.

#### Beispiel mit Standardparametern
```python
def begruessung(name="Teilnehmer"):
    print(f"Hallo, {name}!")

# Mit Standardwert
begruessung()
# Mit Argument
begruessung("Anna")
```

**Ausgabe:**
```
Hallo, Teilnehmer!
Hallo, Anna!
```

### Keyword-Argumente
Beim Funktionsaufruf können Parameter explizit mit Namen angegeben werden, was die Lesbarkeit erhöht.

#### Beispiel
```python
def konto_info(name, betrag):
    print(f"{name} hat ein Konto mit einem Betrag von {betrag}€.")

konto_info(betrag=1000, name="Max")
```

**Ausgabe:**
```
Max hat ein Konto mit einem Betrag von 1000€.
```