## Einsatz von break, continue und pass

### 1. `break`
Die `break`-Anweisung beendet die Ausführung der innersten Schleife vorzeitig. Sie wird häufig verwendet, um eine Schleife bei Eintreten einer bestimmten Bedingung zu beenden.

#### Beispiel:
```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Ausgabe: 0 1 2 3 4
```
In diesem Beispiel wird die Schleife abgebrochen, sobald `i` den Wert 5 erreicht.

### 2. `continue`
Die `continue`-Anweisung überspringt den aktuellen Schleifendurchlauf und fährt mit dem nächsten fort. Sie wird verwendet, um bestimmte Iterationen zu überspringen, ohne die Schleife zu beenden.

#### Beispiel:
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Ausgabe: 1 3 5 7 9
```
Hier werden alle geraden Zahlen übersprungen, und nur die ungeraden Zahlen werden ausgegeben.

### 3. `pass`
Die `pass`-Anweisung ist ein Platzhalter, der keine Aktion ausführt. Sie wird häufig verwendet, um leere Codeblöcke zu definieren, die später implementiert werden sollen.

#### Beispiel:
```python
for i in range(5):
    if i == 3:
        pass  # Platzhalter für zukünftigen Code
    else:
        print(i)
# Ausgabe: 0 1 2 4
```
`pass` hat keinen Einfluss auf den Programmablauf und dient nur als leeres Statement.

## Fallstricke bei Sprunganweisungen

Obwohl Sprunganweisungen nützlich sind, gibt es einige typische Fallstricke, die vermieden werden sollten:

### 1. Übermäßiger Einsatz von `break` und `continue`
Ein häufiger Fehler ist der übermäßige Einsatz von `break` und `continue`, der den Code schwer lesbar macht. Zu viele Sprunganweisungen können die Logik der Schleife kompliziert und unverständlich machen.

#### Beispiel:
```python
for i in range(10):
    if i < 5:
        continue
    if i > 7:
        break
    print(i)
# Ausgabe: 5 6 7
```
Der Code funktioniert, ist aber schwer nachvollziehbar. Eine bessere Alternative könnte die Nutzung klarerer Bedingungen sein.

### 2. `pass` als Platzhalter vergessen
Wenn `pass` als Platzhalter verwendet wird, kann es leicht übersehen werden, den endgültigen Code zu implementieren.

#### Problematisches Beispiel:
```python
def wichtige_funktion():
    pass  # TODO: Implementieren
```
Wenn der Platzhalter nicht entfernt wird, kann die Funktion leer bleiben und zu unerwartetem Verhalten führen.

### 3. `break` in geschachtelten Schleifen
`break` beendet nur die innerste Schleife. Wenn geschachtelte Schleifen abgebrochen werden sollen, muss zusätzliche Logik verwendet werden.

#### Problematisches Beispiel:
```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
# Ausgabe:
# 0 0
# 1 0
# 2 0
```
Hier wird nur die innere Schleife unterbrochen. Falls beide Schleifen abgebrochen werden sollen, kann eine Flag-Variable oder ein `return` in einer Funktion verwendet werden.

### 4. Unbeabsichtigte Auswirkungen auf Schleifenlogik
Sprunganweisungen können die Logik einer Schleife beeinflussen und zu schwer nachvollziehbarem Verhalten führen.

#### Beispiel:
```python
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x)
# Ausgabe: 1 3 5 7 9
```
Die Schleifenlogik funktioniert, aber die Bedingung in Kombination mit `continue` kann verwirrend wirken.
