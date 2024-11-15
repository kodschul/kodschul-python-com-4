## Prioritäten zwischen Operatoren verstehen

Python hat eine feste Hierarchie, die definiert, wie Operatoren in einem Ausdruck ausgewertet werden. Diese Prioritäten bestimmen die Reihenfolge der Auswertung, wenn keine Klammern verwendet werden.

### Wichtigste Operatoren und ihre Prioritäten:
| **Operator**            | **Beschreibung**                   | **Priorität (hoch nach niedrig)** |
|--------------------------|-------------------------------------|-----------------------------------|
| `()`                    | Klammern                           | Höchste                          |
| `**`                    | Potenzierung                       | Sehr hoch                        |
| `*`, `/`, `//`, `%`     | Multiplikation, Division, Modulo   | Hoch                             |
| `+`, `-`                | Addition, Subtraktion              | Mittel                           |
| `<`, `<=`, `>`, `>=`    | Vergleichsoperatoren               | Niedrig                          |
| `==`, `!=`              | Gleichheitsoperatoren              | Niedriger                        |
| `and`                   | Logisches UND                      | Sehr niedrig                     |
| `or`                    | Logisches ODER                     | Niedrigste                       |

### Beispiel: Auswertung ohne Klammern
Betrachten Sie den Ausdruck:
```python
result = 5 + 3 * 2 ** 2
print(result)
```

Schrittweise Auswertung:
1. **Potenzierung**: `2 ** 2` ergibt `4`.
2. **Multiplikation**: `3 * 4` ergibt `12`.
3. **Addition**: `5 + 12` ergibt `17`.

**Ausgabe**:
```
17
```

## Kombinierte Ausdrücke korrekt schreiben

Beim Arbeiten mit komplexeren Ausdrücken ist es wichtig, die Prioritäten der Operatoren zu kennen und Klammern sinnvoll einzusetzen, um die Lesbarkeit und Korrektheit sicherzustellen.

### 1. Verwendung von Klammern zur Klarheit
Durch das Hinzufügen von Klammern können Sie die Reihenfolge der Auswertung explizit steuern:
```python
result = (5 + 3) * 2
print(result)
```
Hier wird zuerst `(5 + 3)` zu `8` ausgewertet, bevor die Multiplikation erfolgt.

**Ausgabe**:
```
16
```

### 2. Vermeidung von Mehrdeutigkeit
In logischen Ausdrücken kann der Vorrang von `and` und `or` leicht zu Verwirrung führen:
```python
result = True or False and False
print(result)
```
Hier wird aufgrund des Vorrangs `and` zuerst ausgewertet:
- `False and False` ergibt `False`.
- Danach: `True or False` ergibt `True`.

**Ausgabe**:
```
True
```

Um dies zu verdeutlichen, verwenden Sie Klammern:
```python
result = (True or False) and False
print(result)
```

Hier wird zuerst `(True or False)` zu `True`, und dann `True and False` zu `False`.

**Ausgabe**:
```
False
```

### 3. Komplexe Berechnungen mit mehreren Operatoren
Kombinierte Ausdrücke mit mehreren Operatoren können fehleranfällig sein, wenn der Vorrang nicht korrekt verstanden wird. Beispiel:
```python
value = 10 - 4 + 3 * 2 / (1 + 1) ** 2
print(value)
```

Schrittweise Auswertung:
1. **Klammern**: `(1 + 1)` ergibt `2`.
2. **Potenzierung**: `2 ** 2` ergibt `4`.
3. **Division**: `3 * 2 / 4` ergibt `1.5`.
4. **Addition und Subtraktion**: `10 - 4 + 1.5` ergibt `7.5`.

**Ausgabe**:
```
7.5
```

### 4. Richtige Anwendung in der Praxis
- Verwenden Sie Klammern, um die Logik klar zu machen, insbesondere in komplexen Ausdrücken.
- Schreiben Sie Ihre Ausdrücke in kleinen, verständlichen Schritten, wenn sie schwer zu lesen sind.

Beispiel:
```python
# Ohne Klammern - schwer lesbar
result = 100 / 5 + 2 * 3 - 1

# Mit Klammern - klarer
result = (100 / 5) + (2 * 3) - 1
```