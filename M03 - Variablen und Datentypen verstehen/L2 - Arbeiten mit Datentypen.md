## Datentyp bestimmen und umwandeln

Python bietet eine Vielzahl von Datentypen, darunter:
- **Primäre Datentypen**: `int`, `float`, `str`, `bool`
- **Komplexere Datentypen**: `list`, `tuple`, `dict`, `set`

### Bestimmung eines Datentyps
Der Datentyp eines Objekts kann mit der Funktion `type()` überprüft werden:
```python
# Beispiel
x = 42
print(type(x))  # Ausgabe: <class 'int'>

y = "Hallo, Welt!"
print(type(y))  # Ausgabe: <class 'str'>
```

### Umwandlung von Datentypen
Python ermöglicht die einfache Umwandlung zwischen verschiedenen Datentypen:
```python
# Umwandlung in einen String
zahl = 123
text = str(zahl)
print(text, type(text))  # Ausgabe: 123 <class 'str'>

# Umwandlung in eine Zahl
text = "3.14"
zahl = float(text)
print(zahl, type(zahl))  # Ausgabe: 3.14 <class 'float'>

# Umwandlung in eine Liste
text = "Python"
liste = list(text)
print(liste, type(liste))  # Ausgabe: ['P', 'y', 't', 'h', 'o', 'n'] <class 'list'>
```

### Häufige Umwandlungsfunktionen
- `int()`: Wandelt ein Objekt in einen Integer um.
- `float()`: Wandelt ein Objekt in einen Float um.
- `str()`: Wandelt ein Objekt in einen String um.
- `list()`, `tuple()`, `set()`, `dict()`: Wandeln Objekte in entsprechende Container-Typen um.

## Dynamische Typisierung in Python

Python ist eine **dynamisch typisierte Sprache**, was bedeutet, dass der Datentyp einer Variablen zur Laufzeit festgelegt wird. Dies macht Python flexibel, erfordert jedoch ein gutes Verständnis der Typensicherheit.

### Beispiele für dynamische Typisierung
```python
# Eine Variable kann unterschiedliche Typen annehmen
x = 10          # x ist ein Integer
print(type(x))  # Ausgabe: <class 'int'>

x = "Hallo"     # x ist jetzt ein String
print(type(x))  # Ausgabe: <class 'str'>
```

### Vorteile der dynamischen Typisierung
- **Flexibilität**: Variablen können während der Laufzeit geändert werden.
- **Einfachheit**: Kein explizites Deklarieren von Datentypen erforderlich.

### Herausforderungen der dynamischen Typisierung
- **Fehleranfälligkeit**: Unerwartete Typänderungen können zu Fehlern führen.
- **Performance**: Dynamische Typisierung kann die Geschwindigkeit der Programmausführung verringern.

### Umgang mit dynamischer Typisierung
Python bietet verschiedene Möglichkeiten, um die Dynamik zu kontrollieren:
1. **Typprüfung vor Operationen**:
   ```python
   x = "123"
   if isinstance(x, str):
       print("x ist ein String")
   ```

2. **Typannotationen (ab Python 3.5)**:
   Typannotationen helfen, den Code klarer zu dokumentieren:
   ```python
   def addiere(a: int, b: int) -> int:
       return a + b
   ```

   Diese Annotationen sind jedoch rein informativ und werden zur Laufzeit nicht überprüft.

3. **Type Checking mit Tools**:
   Tools wie `mypy` können verwendet werden, um Typfehler in statischen Analysen zu erkennen:
   ```bash
   pip install mypy
   mypy mein_programm.py
   ```