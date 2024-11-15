## Die Bedeutung von Leerzeichen in Python

Python ist bekannt für seine klare und lesbare Syntax, bei der **Leerzeichen** eine wichtige Rolle spielen. Sie beeinflussen die Struktur und Lesbarkeit des Codes und sind essenziell für die Funktionsweise bestimmter Konstrukte wie Schleifen und Bedingungen.

### 1. Einrückung in Python
- Python verwendet Leerzeichen (Spaces) oder Tabs für die Einrückung, um Blöcke zu definieren.
- **Beispiel**:
  ```python
  def begrüßung():
      print("Hallo Welt!")  # Dieser Codeblock ist durch Leerzeichen eingerückt

  begrüßung()
  ```
- **Wichtig**: Die Anzahl der Leerzeichen muss innerhalb eines Blocks konsistent sein. Python wirft einen **IndentationError**, wenn die Einrückung nicht einheitlich ist.

### 2. Leerzeichen in Funktions- und Methodenaufrufen
- Leerzeichen können die Lesbarkeit von Code verbessern, sind jedoch in Funktionsaufrufen optional.
- **Ohne Leerzeichen**:
  ```python
  summe = addieren(1,2)
  ```
- **Mit Leerzeichen** (empfohlen):
  ```python
  summe = addieren(1, 2)
  ```

### 3. PEP 8: Style Guide für Python Code
PEP 8 empfiehlt die Verwendung von 4 Leerzeichen pro Einrückungsebene:
- **Beispiel**:
  ```python
  for i in range(5):
      print(i)
  ```

## Trennzeichen und deren Funktion

Trennzeichen in Python sind Symbole oder Zeichenfolgen, die verschiedene Elemente eines Programms voneinander trennen. Sie spielen eine wesentliche Rolle bei der Strukturierung von Daten und der Steuerung von Programmen.

### 1. Kommas als Trennzeichen
- Kommas werden häufig verwendet, um Elemente in Listen, Tupeln oder Argumenten zu trennen.
- **Beispiel**:
  ```python
  liste = [1, 2, 3, 4]
  tupel = (5, 6, 7, 8)
  def funktion(a, b, c):
      return a + b + c
  ```

### 2. Trennzeichen bei Zeichenketten
- Die Methode `split()` teilt eine Zeichenkette an einem bestimmten Trennzeichen auf.
- **Beispiel**:
  ```python
  text = "Apfel, Banane, Kirsche"
  obst_liste = text.split(", ")  # ['Apfel', 'Banane', 'Kirsche']
  ```

### 3. Trennzeichen in Dateipfaden
- Plattformabhängig können verschiedene Trennzeichen für Dateipfade verwendet werden:
  - Windows: Backslash `\`
  - Unix/Linux: Slash `/`
- Python bietet das Modul `os`, um plattformunabhängige Pfade zu verwenden.
- **Beispiel**:
  ```python
  import os
  pfad = os.path.join("verzeichnis", "datei.txt")
  print(pfad)  # Ausgabe ist plattformabhängig
  ```

### 4. Trennzeichen bei CSV-Dateien
- CSV-Dateien verwenden Kommas (oder andere Trennzeichen wie Semikolon) zur Strukturierung von Daten.
- **Beispiel mit dem Modul `csv`**:
  ```python
  import csv
  with open('daten.csv', mode='r') as file:
      reader = csv.reader(file, delimiter=',')
      for zeile in reader:
          print(zeile)
  ```
