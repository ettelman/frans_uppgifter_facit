"""Skapa en klass Person med attributen name och age.

Använd en while-loop med input för att ta emot användarens namn och ålder.

Validera att åldern är ett heltal

Skapa och skriv ut ett Person-objekt om inputen är giltig.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}: {self.age}"
    
while True:
    name = input("Ange ditt namn: ")
    try:
        age_input = int(input("Ange din ålder:"))
        person = Person(name, age_input)
        print(person)
        break
    except ValueError:
        print("Ogiltig ålder, ange ett heltal")