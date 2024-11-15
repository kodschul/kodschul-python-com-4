# Python Schulung: Arbeiten mit Python-Quelltexten

In dieser Schulung werden grundlegende Konzepte zur Arbeit mit Python-Quelltexten behandelt. Sie lernen, wie Sie Anweisungen in Quelltextdateien auslagern, diese ausführen und testen sowie die Nutzung von Entwicklungswerkzeugen wie IDLE und Jupyter Notebook.

## Anweisungen in Quelltext auslagern

Anstatt Anweisungen direkt in der Python-Interpreter-Shell auszuführen, können Sie diese in Quelltextdateien speichern, die mit der Endung `.py` versehen sind.

### Beispiel:
Erstellen Sie eine Datei `example.py` mit folgendem Inhalt:
```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
```

### Vorteile der Auslagerung:
- **Wiederverwendbarkeit**: Der Code kann in verschiedenen Projekten oder Kontexten erneut verwendet werden.
- **Organisation**: Hilft, komplexen Code in kleinere, verständlichere Einheiten zu zerlegen.
- **Versionierung**: Quelltextdateien können leicht mit Versionskontrollsystemen wie Git verwaltet werden.

## Quelltextdateien ausführen und testen

### Ausführen von Python-Dateien
Um eine Python-Datei auszuführen, verwenden Sie das Kommando:
```bash
python example.py
```

### Testen von Funktionen
Zum Testen von Funktionen bietet Python verschiedene Ansätze:

1. **Direkte Tests im Code**:
   Ergänzen Sie den Code durch spezifische Testaufrufe:
   ```python
   if __name__ == "__main__":
       assert greet("Alice") == "Hello, Alice!"
       print("All tests passed.")
   ```

2. **Automatisiertes Testen mit `unittest`**:
   Erstellen Sie eine separate Testdatei `test_example.py`:
   ```python
   import unittest
   from example import greet

   class TestGreet(unittest.TestCase):
       def test_greet(self):
           self.assertEqual(greet("Alice"), "Hello, Alice!")
           self.assertEqual(greet("Bob"), "Hello, Bob!")

   if __name__ == "__main__":
       unittest.main()
   ```

   Führen Sie die Tests aus mit:
   ```bash
   python -m unittest test_example.py
   ```

## Einführung in IDLE und Jupyter Notebook

### IDLE: Die integrierte Entwicklungsumgebung von Python
IDLE ist ein einfacher Editor, der mit Python geliefert wird und sowohl zum Schreiben als auch zum Ausführen von Python-Code verwendet werden kann.

- **Vorteile von IDLE**:
  - Einfache Bedienung, ideal für Einsteiger.
  - Syntax-Highlighting und integrierte Shell.
  - Direkte Ausführung von Python-Dateien.

- **So starten Sie IDLE**:
  Rufen Sie IDLE aus dem Startmenü auf oder führen Sie im Terminal `idle` aus.

### Jupyter Notebook: Interaktive Python-Umgebung
Jupyter Notebook ist ein leistungsfähiges Tool, das es ermöglicht, Python-Code in interaktiven Zellen auszuführen und Ergebnisse in Echtzeit anzuzeigen. Es eignet sich besonders für Datenanalyse und Visualisierung.

1. **Installation**:
   Installieren Sie Jupyter Notebook mit:
   ```bash
   pip install notebook
   ```

2. **Starten des Notebooks**:
   Führen Sie folgenden Befehl aus:
   ```bash
   jupyter notebook
   ```
   Ein Browserfenster öffnet sich, in dem Sie Notebooks erstellen und verwalten können.

3. **Beispiel für ein Notebook**:
   - Schreiben Sie in eine Zelle:
     ```python
     def square(x):
         return x * x

     square(5)
     ```
   - Führen Sie die Zelle aus, um das Ergebnis anzuzeigen.

4. **Erweiterte Funktionen**:
   - **Visualisierung**: Kombinieren Sie Python-Code mit Bibliotheken wie Matplotlib und Pandas.
   - **Markdown-Support**: Dokumentieren Sie Ihren Code direkt im Notebook.