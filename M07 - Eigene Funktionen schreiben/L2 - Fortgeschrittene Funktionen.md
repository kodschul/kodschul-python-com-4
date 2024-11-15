## Globale Variablen und Closures

### Globale Variablen
Globale Variablen sind Variablen, die außerhalb von Funktionen definiert sind und in jeder Funktion innerhalb des Moduls verwendet werden können.

#### Beispiel:
```python
# Globale Variable
x = 10

def print_global():
    print(f"Global variable x: {x}")

print_global()  # Ausgabe: Global variable x: 10
```

### Zugriff auf globale Variablen in Funktionen
Um eine globale Variable innerhalb einer Funktion zu verändern, muss diese mit dem Schlüsselwort `global` deklariert werden:
```python
x = 10

def modify_global():
    global x
    x += 5

modify_global()
print(x)  # Ausgabe: 15
```

### Closures
Closures sind Funktionen, die auf Variablen aus ihrer umgebenden Funktion zugreifen können, selbst wenn die äußere Funktion beendet wurde.

#### Beispiel:
```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure(5))  # Ausgabe: 15
```

In diesem Beispiel speichert das `inner_function` die Variable `x`, die in der äußeren Funktion definiert wurde.

### Vorteile von Closures:
- Datenkapselung
- Zustandsbewahrung ohne globale Variablen

## Lambda-Ausdrücke und anonyme Funktionen

### Lambda-Ausdrücke
Lambda-Ausdrücke sind anonyme Funktionen in Python, die mit dem Schlüsselwort `lambda` erstellt werden. Sie werden häufig für einfache, einmalige Aufgaben verwendet.

#### Syntax:
```python
lambda argumente: ausdruck
```

#### Beispiel:
```python
add = lambda x, y: x + y
print(add(5, 3))  # Ausgabe: 8
```

### Verwendung von Lambda-Ausdrücken
Lambda-Ausdrücke sind besonders nützlich in Kombination mit Funktionen wie `map()`, `filter()` und `sorted()`.

#### Beispiel mit `map()`:
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Ausgabe: [1, 4, 9, 16]
```

#### Beispiel mit `filter()`:
```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Ausgabe: [2, 4]
```

#### Beispiel mit `sorted()`:
```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Ausgabe: [(1, 'one'), (3, 'three'), (2, 'two')]
```