Program przeznaczony jest do zastosowania w obszarze logistyki i transportu.
Pomaga użytkownikowi zaplanować ułożenie ładunku na standardowej naczepie typu "TIR".
Użytkownik posiada dwie możliwość wprowadzenia danych o ładunku (wymiary paczek, waga):
A. Eksport pliku tekstowego z danymi,
B. Manualne wprowadzenie danych o każdej jednostce ładunku.

Algorytm bazuje na modelu MVC i składa się z 4 klas:
1. class View: interfejs użytkownika; rozpoczęcie programu, wyświetlenie wyniku końcowego.
2. class Model_A: wprowadzenie i analiza spójność danych otrzymanych od użytkownika (wybór A).
3. class Model_B: wprowadzenie i analiza spójność danych otrzymanych od użytkownika (wybór B).
4. class Controller: sortowanie danych.





ENGLISH

The program is applicable in the logistics area.
It helps user (transport planner) to draft a cargo placement on standard trailer truck 24t.
User has two options to input cargo data (dimensions, weight):
A. Upload of a text file,
B. Manual data entry of each box.

The algorythm uses MVC model. It consists of 4 classes:
1. class View: user interface; program start and end-output.
2. class Model_A: entry and data cleaning (user's choice A).
3. class Model_B: entry and data cleaning (user's choice B).
4. class Controller: data sorting.
