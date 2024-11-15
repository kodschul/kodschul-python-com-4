## Entscheidungsanweisungen: if, else, elif

Entscheidungsanweisungen werden verwendet, um basierend auf Bedingungen unterschiedliche Programmzweige auszuführen.

### if-Anweisung
Die einfachste Form der Entscheidungsanweisung ist die `if`-Anweisung. Sie überprüft eine Bedingung und führt den nachfolgenden Block nur aus, wenn die Bedingung wahr ist.
```python
# Beispiel: Überprüfung einer Bedingung
x = 10
if x > 5:
    print("x ist größer als 5")
```

### if-else-Anweisung
Die `if-else`-Anweisung ermöglicht das Ausführen eines Alternativblocks, wenn die Bedingung nicht erfüllt ist.
```python
# Beispiel: Bedingung mit Alternativblock
x = 3
if x > 5:
    print("x ist größer als 5")
else:
    print("x ist 5 oder kleiner")
```

### if-elif-else-Anweisung
Mit der `elif`-Anweisung (kurz für "else if") können mehrere Bedingungen überprüft werden.
```python
# Beispiel: Mehrere Bedingungen überprüfen
x = 7
if x > 10:
    print("x ist größer als 10")
elif x > 5:
    print("x ist größer als 5 aber kleiner oder gleich 10")
else:
    print("x ist 5 oder kleiner")
```

## Iterationsanweisungen: for- und while-Schleifen

Schleifen werden verwendet, um einen Codeblock mehrfach auszuführen.

### for-Schleifen
Die `for`-Schleife wird verwendet, um über Sequenzen (z.B. Listen, Tupel, Strings) oder Bereiche (Ranges) zu iterieren.

#### Iterieren über eine Liste
```python
# Beispiel: Schleife durch eine Liste
zahlen = [1, 2, 3, 4, 5]
for zahl in zahlen:
    print(zahl)
```

#### Iterieren über einen Bereich
```python
# Beispiel: Schleife durch einen Bereich
for i in range(5):  # 0 bis 4
    print(f"Zahl: {i}")
```

### while-Schleifen
Die `while`-Schleife wird verwendet, um einen Codeblock auszuführen, solange eine Bedingung wahr ist.

#### Beispiel: Schleife mit Bedingung
```python
# Beispiel: Schleife mit Bedingung
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
```

#### Endlosschleifen vermeiden
Wenn die Bedingung einer `while`-Schleife niemals `False` wird, entsteht eine Endlosschleife. Verwenden Sie Kontrollanweisungen wie `break`, um Schleifen zu verlassen.
```python
# Beispiel: Schleife abbrechen
count = 0
while True:
    print(f"Count: {count}")
    count += 1
    if count == 5:
        break
```