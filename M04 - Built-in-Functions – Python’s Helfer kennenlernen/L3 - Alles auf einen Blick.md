## Überblick über Built-in-Functions

Python bietet eine Vielzahl von integrierten Funktionen, die direkt ohne zusätzliche Importe verwendet werden können. Diese Funktionen decken häufige Aufgaben ab und sparen Zeit beim Entwickeln.

### Beispiele für wichtige Built-in-Functions:

1. **Arbeiten mit Listen und Iterables**:
   - `len()`: Gibt die Länge eines Objekts zurück.
   - `sum()`: Addiert die Werte in einem Iterable.
   - `max()`, `min()`: Gibt den größten bzw. kleinsten Wert eines Iterables zurück.
   - `sorted()`: Gibt eine sortierte Version eines Iterables zurück.

   ```python
   numbers = [3, 1, 4, 1, 5]
   print(len(numbers))  # 5
   print(sum(numbers))  # 14
   print(max(numbers))  # 5
   print(sorted(numbers))  # [1, 1, 3, 4, 5]
   ```

2. **Typumwandlungen**:
   - `int()`, `float()`, `str()`, `bool()`: Wandelt Werte in verschiedene Typen um.
   - `list()`, `tuple()`, `set()`, `dict()`: Konvertiert in andere Datenstrukturen.

   ```python
   value = "42"
   print(int(value))  # 42
   print(float(value))  # 42.0
   print(list(value))  # ['4', '2']
   ```

3. **Eingabe und Ausgabe**:
   - `print()`: Gibt Daten auf der Konsole aus.
   - `input()`: Liest Benutzereingaben als String ein.

   ```python
   name = input("Wie heißt du? ")
   print(f"Hallo, {name}!")
   ```

4. **Arbeiten mit Funktionen und Iterables**:
   - `map()`, `filter()`: Wenden Funktionen auf Iterables an.
   - `zip()`: Kombiniert mehrere Iterables zu einem.
   - `enumerate()`: Fügt einem Iterable Indizes hinzu.

   ```python
   numbers = [1, 2, 3, 4]
   doubled = map(lambda x: x * 2, numbers)
   print(list(doubled))  # [2, 4, 6, 8]

   evens = filter(lambda x: x % 2 == 0, numbers)
   print(list(evens))  # [2, 4]
   ```

5. **Fehlerbehandlung**:
   - `isinstance()`: Prüft, ob ein Objekt einen bestimmten Typ hat.
   - `callable()`: Prüft, ob ein Objekt aufrufbar ist (z.B. eine Funktion).

   ```python
   value = 42
   print(isinstance(value, int))  # True
   print(callable(print))  # True
   ```

## Effizienter Einsatz von Funktionen in Python

Der effiziente Einsatz von Funktionen ermöglicht es, Code eleganter, lesbarer und wartbarer zu gestalten.

### Tipps für den Einsatz von Built-in-Functions:

1. **Kombination von Funktionen**:
   Built-in-Functions können häufig kombiniert werden, um komplexe Aufgaben zu lösen.

   ```python
   words = ["Python", "Schulung", "Effizienz"]
   lengths = map(len, words)
   print(sum(lengths))  # 24
   ```

2. **Vermeidung von Schleifen**:
   Viele Built-in-Functions wie `map()` und `filter()` ersetzen die Notwendigkeit von expliziten Schleifen.

   ```python
   numbers = [1, 2, 3, 4]
   squares = [x**2 for x in numbers]  # List Comprehension
   print(squares)  # [1, 4, 9, 16]
   ```

3. **Verwendung von `lambda` für Ad-hoc-Funktionen**:
   Lambda-Ausdrücke eignen sich gut für kurze Funktionen, die nur einmal verwendet werden.

   ```python
   numbers = [1, 2, 3, 4]
   doubled = map(lambda x: x * 2, numbers)
   print(list(doubled))  # [2, 4, 6, 8]
   ```

4. **Nutzen von `any()` und `all()` für Bedingungen**:
   - `any()`: Gibt True zurück, wenn irgendein Wert wahr ist.
   - `all()`: Gibt True zurück, wenn alle Werte wahr sind.

   ```python
   conditions = [True, False, True]
   print(any(conditions))  # True
   print(all(conditions))  # False
   ```

### Performance-Optimierung:
- Verwenden Sie Built-in-Functions, da diese in C implementiert und dadurch oft schneller als eigene Implementierungen sind.
- Vermeiden Sie unnötige Typkonvertierungen und nutzen Sie Generatoren, um Speicher effizient zu nutzen.
