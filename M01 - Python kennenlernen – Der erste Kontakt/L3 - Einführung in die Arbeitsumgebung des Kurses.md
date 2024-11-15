# Python Schulung: Python-Tools und Umgebungen

In dieser Schulung wird gezeigt, wie man effektive Werkzeuge und Umgebungen für die Python-Entwicklung nutzt. Der Fokus liegt auf Anaconda, Jupyter Notebook und dem Umgang mit den integrierten Hilfefunktionen von Python sowie Befehlszeilentools.

## Anaconda installieren und nutzen

Anaconda ist eine Open-Source-Distribution für Python und R, die speziell für Datenanalyse, maschinelles Lernen und wissenschaftliches Rechnen entwickelt wurde.

### Schritte zur Installation von Anaconda
1. **Download**:
   - Besuchen Sie die [Anaconda-Website](https://www.anaconda.com/) und laden Sie die Version herunter, die mit Ihrem Betriebssystem kompatibel ist.

2. **Installation**:
   - Folgen Sie den Anweisungen des Installationsprogramms, um Anaconda auf Ihrem System zu installieren.

3. **Überprüfung der Installation**:
   - Öffnen Sie ein Terminal oder die Anaconda Prompt und geben Sie den folgenden Befehl ein:
     ```bash
     conda --version
     ```

### Nutzen von Anaconda
- **Conda-Umgebungen verwalten**:
  - Erstellen Sie isolierte Umgebungen für verschiedene Projekte:
    ```bash
    conda create --name myenv python=3.9
    conda activate myenv
    ```
- **Pakete installieren**:
  - Installieren Sie Python-Bibliotheken und Abhängigkeiten:
    ```bash
    conda install numpy pandas
    ```

## Jupyter Notebook für interaktive Programmierung

Jupyter Notebook ist eine Open-Source-Webanwendung, die es ermöglicht, Python-Code in interaktiven Zellen zu schreiben, auszuführen und zu dokumentieren.

### Installation und Start von Jupyter Notebook
1. **Installation**:
   - Installieren Sie Jupyter Notebook mit pip oder conda:
     ```bash
     conda install jupyter
     ```

2. **Starten von Jupyter Notebook**:
   - Starten Sie die Anwendung in einem Terminal:
     ```bash
     jupyter notebook
     ```
   - Ein Browserfenster öffnet sich, in dem Sie neue Notebooks erstellen und bearbeiten können.

### Grundlagen der Nutzung
- **Code-Zellen ausführen**:
  - Schreiben Sie Python-Code in eine Zelle und führen Sie ihn mit `Shift + Enter` aus.
- **Markdown-Zellen**:
  - Verwenden Sie Markdown-Zellen, um Text, Überschriften oder Formatierungen hinzuzufügen.
- **Plotten von Diagrammen**:
  - Integrieren Sie Bibliotheken wie Matplotlib und Seaborn, um Daten zu visualisieren:
    ```python
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.show()
    ```

## Hilfemodus und Befehlszeilentools kennenlernen

Python bietet verschiedene Möglichkeiten, Hilfe zu Funktionen und Modulen direkt in der Konsole oder im Skript zu erhalten.

### Hilfemodus in Python
- **help() Funktion**:
  - Geben Sie den Namen eines Moduls oder einer Funktion in `help()` ein, um Dokumentationen anzuzeigen:
    ```python
    help(print)
    ```
- **dir() Funktion**:
  - Verwenden Sie `dir()`, um alle Attribute und Methoden eines Objekts aufzulisten:
    ```python
    dir(str)
    ```

### Nutzung von Befehlszeilentools
- **Python-Interpreter**:
  - Starten Sie den Python-Interpreter in der Konsole:
    ```bash
    python
    ```
- **Skripte ausführen**:
  - Führen Sie Python-Skripte direkt über die Befehlszeile aus:
    ```bash
    python script.py
    ```
- **Pip für Paketmanagement**:
  - Installieren Sie Python-Pakete mit pip:
    ```bash
    pip install requests
    ```
