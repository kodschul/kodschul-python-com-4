## Arithmetische und logische Operatoren

### Arithmetische Operatoren
Arithmetische Operatoren werden verwendet, um mathematische Berechnungen durchzuführen. Python unterstützt die folgenden Operatoren:

| Operator | Beschreibung       | Beispiel         | Ergebnis |
|----------|--------------------|------------------|----------|
| `+`      | Addition           | `2 + 3`          | `5`      |
| `-`      | Subtraktion        | `7 - 2`          | `5`      |
| `*`      | Multiplikation     | `3 * 4`          | `12`     |
| `/`      | Division           | `10 / 2`         | `5.0`    |
| `//`     | Ganzzahl-Division  | `10 // 3`        | `3`      |
| `%`      | Modulo (Rest)      | `10 % 3`         | `1`      |
| `**`     | Potenzierung       | `2 ** 3`         | `8`      |

### Beispiele:
```python
a = 10
b = 3
print(a + b)   # Addition: 13
print(a // b)  # Ganzzahl-Division: 3
print(a ** b)  # Potenzierung: 1000
```

### Logische Operatoren
Logische Operatoren werden verwendet, um boolesche Ausdrücke zu verknüpfen.

| Operator | Beschreibung     | Beispiel                 | Ergebnis |
|----------|------------------|--------------------------|----------|
| `and`    | Logisches UND    | `True and False`         | `False`  |
| `or`     | Logisches ODER   | `True or False`          | `True`   |
| `not`    | Logisches NICHT  | `not True`               | `False`  |

### Beispiele:
```python
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

---

## Vergleichs- und Zuweisungsoperatoren

### Vergleichsoperatoren
Vergleichsoperatoren werden verwendet, um Werte zu vergleichen. Sie geben immer einen booleschen Wert zurück.

| Operator | Beschreibung                | Beispiel        | Ergebnis |
|----------|-----------------------------|-----------------|----------|
| `==`     | Gleich                      | `5 == 5`        | `True`   |
| `!=`     | Ungleich                    | `5 != 3`        | `True`   |
| `>`      | Größer                      | `7 > 4`         | `True`   |
| `<`      | Kleiner                     | `4 < 7`         | `True`   |
| `>=`     | Größer oder gleich          | `5 >= 5`        | `True`   |
| `<=`     | Kleiner oder gleich         | `3 <= 8`        | `True`   |

### Beispiele:
```python
x = 10
y = 20
print(x == y)   # False
print(x < y)    # True
```

### Zuweisungsoperatoren
Zuweisungsoperatoren werden verwendet, um Werte Variablen zuzuweisen.

| Operator | Beschreibung                     | Beispiel     | Ergebnis |
|----------|----------------------------------|--------------|----------|
| `=`      | Zuweisung                        | `x = 5`      | `x = 5`  |
| `+=`     | Addition und Zuweisung           | `x += 3`     | `x = 8`  |
| `-=`     | Subtraktion und Zuweisung        | `x -= 2`     | `x = 6`  |
| `*=`     | Multiplikation und Zuweisung     | `x *= 4`     | `x = 24` |
| `/=`     | Division und Zuweisung           | `x /= 2`     | `x = 12` |
| `//=`    | Ganzzahl-Division und Zuweisung  | `x //= 3`    | `x = 4`  |
| `%=`     | Modulo und Zuweisung             | `x %= 3`     | `x = 1`  |
| `**=`    | Potenzierung und Zuweisung       | `x **= 2`    | `x = 1`  |

### Beispiele:
```python
x = 10
x += 5  # x = 15
x *= 2  # x = 30
print(x)  # 30
```

---