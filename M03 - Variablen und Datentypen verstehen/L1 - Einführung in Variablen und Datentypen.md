## Variablen deklarieren und verwenden

### Was sind Variablen?
Variablen sind Platzhalter für Daten, die im Speicher gespeichert werden. Sie ermöglichen es, Werte zu speichern, zu manipulieren und in Programmen wiederzuverwenden.

### Variablen in Python deklarieren
In Python ist die Deklaration einer Variablen einfach und erfordert keine Typdefinition. Der Typ wird automatisch anhand des zugewiesenen Wertes erkannt.

#### Beispiele:
```python
# Deklaration und Initialisierung
name = "John"          # String
age = 25               # Integer
height = 5.9           # Float
is_student = True      # Boolean

# Ausgabe von Variablen
print(name)            # Ausgabe: John
print(age)             # Ausgabe: 25
print(height)          # Ausgabe: 5.9
print(is_student)      # Ausgabe: True
```

### Regeln für Variablennamen
1. Variablennamen dürfen Buchstaben, Zahlen und Unterstriche enthalten, aber nicht mit einer Zahl beginnen.
2. Variablennamen sind case-sensitive (`Name` und `name` sind unterschiedliche Variablen).
3. Vermeiden Sie reservierte Wörter wie `if`, `else`, `while` usw.

### Variablen manipulieren
Variablen können verwendet werden, um Werte zu berechnen oder zu ändern.

#### Beispiel:
```python
x = 10
y = 5
sum = x + y          # Addition
difference = x - y   # Subtraktion
product = x * y      # Multiplikation
quotient = x / y     # Division

print(sum, difference, product, quotient)
```

## Die Python-Datentypen im Detail

Python bietet eine Vielzahl von Datentypen, um verschiedene Arten von Daten zu speichern und zu verarbeiten.

### 1. **Primitive Datentypen**
- **Integer** (`int`): Ganze Zahlen
  ```python
  num = 42
  print(type(num))  # Ausgabe: <class 'int'>
  ```
- **Float** (`float`): Dezimalzahlen
  ```python
  pi = 3.14159
  print(type(pi))  # Ausgabe: <class 'float'>
  ```
- **String** (`str`): Text
  ```python
  text = "Hallo, Python!"
  print(type(text))  # Ausgabe: <class 'str'>
  ```
- **Boolean** (`bool`): Wahrheitswerte (`True`, `False`)
  ```python
  is_active = True
  print(type(is_active))  # Ausgabe: <class 'bool'>
  ```

### 2. **Komplexe Datentypen**
- **Liste** (`list`): Sammlung von Elementen in einer bestimmten Reihenfolge
  ```python
  fruits = ["Apple", "Banana", "Cherry"]
  print(fruits[1])  # Ausgabe: Banana
  ```
- **Tupel** (`tuple`): Unveränderliche Liste
  ```python
  coordinates = (10, 20)
  print(coordinates[0])  # Ausgabe: 10
  ```
- **Dictionary** (`dict`): Sammlung von Schlüssel-Wert-Paaren
  ```python
  student = {"name": "Alice", "age": 21}
  print(student["name"])  # Ausgabe: Alice
  ```
- **Set** (`set`): Sammlung von einzigartigen, ungeordneten Elementen
  ```python
  unique_numbers = {1, 2, 3, 4}
  print(3 in unique_numbers)  # Ausgabe: True
  ```

### 3. **Datentyp-Umwandlung**
Python ermöglicht die Umwandlung zwischen verschiedenen Datentypen.

#### Beispiel:
```python
# String in Integer umwandeln
num_str = "123"
num = int(num_str)
print(type(num))  # Ausgabe: <class 'int'>

# Float in String umwandeln
pi = 3.14
pi_str = str(pi)
print(type(pi_str))  # Ausgabe: <class 'str'>
```