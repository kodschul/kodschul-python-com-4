## Python-Interaktivmodus: Erste Befehle ausprobieren

Python verfügt über einen interaktiven Modus, auch bekannt als REPL (Read-Eval-Print Loop), der es ermöglicht, Python-Befehle direkt auszuführen und Ergebnisse sofort zu sehen. Dies ist besonders hilfreich, um kleine Code-Schnipsel zu testen oder die Sprache zu erlernen.

### Python-Interaktivmodus starten
1. Öffnen Sie ein Terminal oder eine Konsole.
2. Geben Sie den Befehl `python` oder `python3` ein (abhängig von Ihrer Installation).
3. Sie befinden sich nun im interaktiven Modus, erkennbar am `>>>`-Prompt.

### Erste Befehle
- **Mathematische Operationen**:
  ```python
  >>> 2 + 2
  4
  >>> 10 / 3
  3.3333333333333335
  ```

- **Variablen erstellen**:
  ```python
  >>> x = 5
  >>> y = 10
  >>> x + y
  15
  ```

- **Strings**:
  ```python
  >>> name = "Python"
  >>> print(f"Hello, {name}!")
  Hello, Python!
  ```

Beenden Sie den Modus mit `exit()` oder durch Drücken von `Ctrl+D`.

## Einrückungen und Zeilenende: Die Struktur verstehen

Python verwendet Einrückungen, um Blöcke von Code zu strukturieren, anstatt geschweifte Klammern `{}` wie in vielen anderen Programmiersprachen.

### Einrückungen in Python
- Python verwendet **Leerzeichen** oder **Tabulatoren** für Einrückungen. Einrückungen sind nicht optional.
- Ein typischer Block wird mit 4 Leerzeichen eingerückt.

Beispiel:
```python
def greet(name):
    print(f"Hello, {name}!")
    print("Welcome to Python.")
```

### Fehler bei falschen Einrückungen
Falsche Einrückungen führen zu einem **IndentationError**:
```python
def greet(name):
print(f"Hello, {name}!")  # Fehler: Keine Einrückung
```

### Zeilenende
Python erkennt das Ende einer Anweisung durch einen Zeilenumbruch. Wenn eine Anweisung zu lang ist, können Sie den Backslash (`\`) verwenden, um sie auf die nächste Zeile fortzusetzen:
```python
total = 1 + 2 + 3 +         4 + 5 + 6
print(total)
```

## Groß- und Kleinschreibung in Python

Python ist **case-sensitive**, was bedeutet, dass Groß- und Kleinschreibung bei Bezeichnern und Variablen eine Rolle spielen.

### Beispiele
```python
Name = "Alice"
name = "Bob"

print(Name)  # Gibt "Alice" aus
print(name)  # Gibt "Bob" aus
```

### Best Practices
- Variablennamen sollten mit Kleinbuchstaben beginnen: `my_variable`
- Konstanten werden in Großbuchstaben geschrieben: `PI = 3.14`

Achten Sie auf die Groß- und Kleinschreibung von **Schlüsselwörtern**:
```python
Print("Hello")  # Fehler: 'Print' existiert nicht, nur 'print'
```

## Fazit

Diese Einführung bietet die ersten Schritte in Python: vom Ausprobieren einfacher Befehle im Interaktivmodus bis hin zur Beherrschung grundlegender Syntaxregeln. Einrückungen, Zeilenende und die Beachtung der Groß- und Kleinschreibung sind essenziell, um Python-Code korrekt und lesbar zu schreiben.
