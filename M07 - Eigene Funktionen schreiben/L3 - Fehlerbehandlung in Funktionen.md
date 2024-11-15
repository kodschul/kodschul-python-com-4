## Fehlerbehandlung in Funktionen

### Warum Fehlerbehandlung wichtig ist
Fehler sind ein natürlicher Bestandteil des Programmierens. Eine gute Fehlerbehandlung ermöglicht es:
- **Abstürze zu vermeiden**: Durch das Abfangen von Fehlern kann verhindert werden, dass das Programm komplett abstürzt.
- **Nutzerfreundlichkeit**: Benutzer erhalten informative Fehlermeldungen, statt kryptischer Fehlermeldungen oder einem Programmabbruch.
- **Einfache Fehlersuche**: Durch gezielte Protokollierung von Fehlern kann die Ursache einfacher analysiert werden.

### Grundlagen der Fehlerbehandlung
In Python wird die Fehlerbehandlung mit den Schlüsselwörtern `try`, `except`, `else` und `finally` durchgeführt.

#### Beispiel:
```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Fehler: Division durch Null ist nicht erlaubt.")
        return None
    else:
        print("Division erfolgreich!")
        return result
    finally:
        print("Funktion divide() wurde ausgeführt.")

# Test der Funktion
print(divide(10, 2))  # Ausgabe: 5.0
print(divide(10, 0))  # Ausgabe: Fehler: Division durch Null
```

#### Schlüsselwörter erklärt:
- **`try`**: Der Code, der potenziell einen Fehler auslösen könnte, wird hier eingefügt.
- **`except`**: Wird ausgeführt, wenn im `try`-Block eine Ausnahme auftritt.
- **`else`**: Wird ausgeführt, wenn im `try`-Block **keine** Ausnahme auftritt.
- **`finally`**: Wird immer ausgeführt, unabhängig davon, ob eine Ausnahme aufgetreten ist oder nicht.

## Best Practices für Fehlerbehandlung in Funktionen

### 1. Abfangen spezifischer Ausnahmen
Fangen Sie nur die spezifischen Ausnahmen ab, die Sie erwarten, anstatt einen generischen `except`-Block zu verwenden.
```python
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden.")
```

### 2. Keine leeren `except`-Blöcke
Vermeiden Sie leere `except`-Blöcke, da sie Fehler stillschweigend ignorieren können.
```python
# Schlechte Praxis
try:
    risky_operation()
except:
    pass  # Keine Meldung, der Fehler bleibt unentdeckt
```

### 3. Protokollierung von Fehlern
Nutzen Sie das `logging`-Modul, um Fehler zu protokollieren, anstatt sie nur auszugeben.
```python
import logging

def risky_operation():
    try:
        # Fehlerhafter Code
        1 / 0
    except ZeroDivisionError as e:
        logging.error("Ein Fehler ist aufgetreten: %s", e)
```

### 4. Verwendung von Ausnahmen für Kontrollfluss vermeiden
Verwenden Sie Ausnahmen nicht für normale Kontrollfluss-Logik, da dies den Code schwer lesbar macht.

### 5. Benutzerdefinierte Ausnahmen
Erstellen Sie eigene Ausnahmen, um spezifische Fehler in Ihrer Anwendung zu behandeln.
```python
class CustomError(Exception):
    pass

def function_with_custom_error(condition):
    if not condition:
        raise CustomError("Bedingung wurde nicht erfüllt.")
```

## Praktische Übung

### Aufgabe: Implementierung einer robusten Funktion
Erstellen Sie eine Funktion `read_file(filename)`, die:
1. Versucht, eine Datei zu öffnen und ihren Inhalt zu lesen.
2. Eine sinnvolle Fehlermeldung ausgibt, falls die Datei nicht existiert.
3. Sicherstellt, dass die Datei, falls sie geöffnet wurde, korrekt geschlossen wird.

#### Beispiel:
```python
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{filename}' wurde nicht gefunden.")
        return None
    finally:
        print("Funktion read_file() wurde ausgeführt.")

# Test
content = read_file("example.txt")
if content:
    print(content)
```