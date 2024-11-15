## Die `print()`- und `input()`-Funktion

### 1. Die `print()`-Funktion
Die `print()`-Funktion wird verwendet, um Ausgaben auf der Konsole darzustellen. Sie ist eine der am häufigsten verwendeten Funktionen in Python.

#### Syntax:
```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

#### Beispiele:
- Einfache Ausgabe:
  ```python
  print("Hallo, Welt!")
  ```
  **Ausgabe**: `Hallo, Welt!`

- Ausgabe mit mehreren Werten:
  ```python
  print("Name:", "Alice", "Alter:", 30)
  ```
  **Ausgabe**: `Name: Alice Alter: 30`

- Anpassung der Trennzeichen (`sep`) und Endzeichen (`end`):
  ```pythona
  print("A", "B", "C", sep="-", end=".")
  ```
  **Ausgabe**: `A-B-C.`

### 2. Die `input()`-Funktion
Die `input()`-Funktion wird verwendet, um Benutzereingaben zu erfassen. Sie gibt die Eingabe als String zurück.

#### Syntax:
```python
input(prompt)
```

#### Beispiele:
- Einfache Eingabe:
  ```python
  name = input("Wie heißt du? ")
  print("Hallo,", name)
  ```
  **Eingabe**: `Alice`
  **Ausgabe**: `Hallo, Alice`

- Verarbeitung von Zahlen (Typkonvertierung erforderlich):
  ```python
  alter = int(input("Wie alt bist du? "))
  print("In 5 Jahren wirst du", alter + 5, "Jahre alt sein.")
  ```
  **Eingabe**: `25`
  **Ausgabe**: `In 5 Jahren wirst du 30 Jahre alt sein.`

---

## Mathematische Umwandlungen und Evaluierungen

Python bietet eine Vielzahl von Funktionen zur mathematischen Verarbeitung und Typkonvertierung.

### 1. Die `int()`, `float()` und `str()`-Funktionen
Diese Funktionen konvertieren Werte in einen bestimmten Datentyp:
- **`int()`**: Konvertiert in eine Ganzzahl.
- **`float()`**: Konvertiert in eine Fließkommazahl.
- **`str()`**: Konvertiert in einen String.

#### Beispiele:
- Ganzzahlen und Fließkommazahlen:
  ```python
  print(int("10"))      # 10
  print(float("3.14"))  # 3.14
  print(str(42))        # '42'
  ```

- Typkonvertierung mit `input()`:
  ```python
  zahl = float(input("Gib eine Zahl ein: "))
  print("Das Doppelte der Zahl ist:", zahl * 2)
  ```
  **Eingabe**: `4.5`
  **Ausgabe**: `Das Doppelte der Zahl ist: 9.0`

### 2. Die `abs()`-Funktion
Die `abs()`-Funktion gibt den Absolutwert einer Zahl zurück.

#### Beispiele:
```python
print(abs(-5))    # 5
print(abs(3.14))  # 3.14
```

### 3. Die `round()`-Funktion
Die `round()`-Funktion rundet eine Zahl auf die angegebene Dezimalstelle.

#### Beispiele:
```python
print(round(3.14159, 2))  # 3.14
print(round(2.718, 1))    # 2.7
```

### 4. Die `pow()`- und `max()`-/`min()`-Funktionen
- **`pow(x, y)`**: Gibt x hoch y zurück.
- **`max()` und `min()`**: Finden das Maximum bzw. Minimum einer Liste oder von Argumenten.

#### Beispiele:
```python
print(pow(2, 3))         # 8
print(max(1, 2, 3, 4))   # 4
print(min(1, 2, 3, 4))   # 1
```

---