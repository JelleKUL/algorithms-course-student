# Hoofdstuk 1: Inleiding tot Python

Dit hoofdstuk dient om je Python-kennis op te frissen. De bedoeling is dat je de
oefeningen **zelf** oplost, zonder gebruik te maken van coding agents of AI-assistenten
die de code voor je schrijven. Voor het eerste deel heb je dan ook nog geen computer nodig.

---

## Oefening 1: Code lezen

Bekijk onderstaande functie aandachtig.

```python
def bereken_reeks(n):
    reeks = [1, 1]
    if n<=2:
        return reeks
    for i in range(n - 2):
        x = reeks[-2] + reeks[-1]
        reeks.append(x)
    return reeks
```

Bereken manueel wat `bereken_reeks(10)` teruggeeft. 
Schrijf het antwoord hieronder neer.

*Tip: volg de variabelen `reeks` en `x` bij elke iteratie van de lus.*

### Antwoord:


<br><br><br><br>
---

<hr class="mde4-pgbrk">

## Oefening 2: Zoek de fout

Hieronder zie je een andere versie van dezelfde functie. Deze versie bevat een fout die
je pas ontdekt als je ze met bepaalde waarden van `n` aanroept.

```python
def bereken_reeks(n):
    reeks = [0] * n
    reeks[0] = 1
    reeks[1] = 1
    for i in range(2, n):
        reeks[i] = reeks[i - 1] + reeks[i - 2]
    return reeks
```

Wanneer je deze functie aanroept met bijvoorbeeld `bereken_reeks(1)`, krijg je volgende
foutmelding te zien:

```
Traceback (most recent call last):
  File "reeks.py", line 8, in <module>
    print(bereken_reeks(1))
  File "reeks.py", line 4, in bereken_reeks
    reeks[1] = 1
    ~~~~~^^^
IndexError: list assignment index out of range
```

Beantwoord onderstaande vragen.

1. Voor welke waarde(n) van `n` loopt deze functie vast?
2. Welk type foutmelding (exception) zie je in Python?
3. Op welke regel in de code gaat het precies fout, en waarom?
4. Hoe zou je de functie aanpassen zodat ze ook voor kleine waarden van `n` (0 of 1)
   correct werkt, zonder te crashen?

### Antwoord:

<br><br><br><br><br>

---