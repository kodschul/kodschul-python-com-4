## Verschachtelte Kontrollstrukturen

In Python können Kontrollstrukturen wie Schleifen und Bedingungen miteinander kombiniert werden, um logische Entscheidungen und wiederholte Ausführungen in einem Programm zu steuern.

### Beispiele für verschachtelte Kontrollstrukturen

1. **Verschachtelte `if`-Bedingungen**:
   ```python
   x = 10
   y = 20

   if x > 5:
       if y > 15:
           print("x ist größer als 5 und y ist größer als 15")
   ```

   - Hier wird eine `if`-Bedingung innerhalb einer anderen `if`-Bedingung verwendet.
   - Solche Verschachtelungen sind hilfreich, wenn mehrere Bedingungen erfüllt sein müssen.

2. **Schleifen in Bedingungen**:
   ```python
   numbers = [1, 2, 3, 4, 5]

   if len(numbers) > 0:
       for num in numbers:
           if num % 2 == 0:
               print(f"{num} ist gerade")
   ```

   - Diese Kombination prüft, ob die Liste Elemente enthält, und iteriert anschließend über die Liste, um gerade Zahlen zu finden.

3. **Schleifen innerhalb von Schleifen**:
   ```python
   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

   for row in matrix:
       for value in row:
           print(value, end=" ")
       print()
   ```

   - Verschachtelte Schleifen sind ideal für die Arbeit mit mehrdimensionalen Datenstrukturen wie Matrizen.

## Komplexe Programmflüsse effizient gestalten

Das effiziente Gestalten von komplexen Programmflüssen erfordert:
- Eine klare Strukturierung der Logik.
- Die Minimierung von tiefen Verschachtelungen.
- Die Nutzung von Funktionen zur Modularisierung.

### Tipps für effiziente Programmflüsse

1. **Verwendung von `elif`**:
   - Statt mehrere verschachtelte `if`-Bedingungen zu verwenden, kann `elif` die Lesbarkeit verbessern.
   ```python
   value = 10
   if value < 5:
       print("Wert ist kleiner als 5")
   elif value == 10:
       print("Wert ist gleich 10")
   else:
       print("Wert ist größer als 10")
   ```

2. **Funktionen zur Modularisierung**:
   - Komplexe Logik kann in Funktionen ausgelagert werden, um den Hauptprogrammfluss übersichtlich zu halten.
   ```python
   def process_number(num):
       if num % 2 == 0:
           return "gerade"
       else:
           return "ungerade"

   numbers = [1, 2, 3, 4, 5]
   for num in numbers:
       print(f"{num} ist {process_number(num)}")
   ```

3. **Liste statt Schleifen kombinieren**:
   - Nutzen Sie List Comprehensions, um Schleifen und Bedingungen zu kombinieren.
   ```python
   numbers = [1, 2, 3, 4, 5]
   even_numbers = [num for num in numbers if num % 2 == 0]
   print("Gerade Zahlen:", even_numbers)
   ```

4. **Fehlerbehandlung mit `try` und `except`**:
   - Fehlerkontrollstrukturen wie `try` und `except` können in komplexen Programmflüssen genutzt werden, um Fehler abzufangen.
   ```python
   try:
       result = 10 / 0
   except ZeroDivisionError:
       print("Division durch Null ist nicht erlaubt")
   ```