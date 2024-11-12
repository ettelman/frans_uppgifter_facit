"""
Kan göras manuellt, men för att det ska bli ett script krävs if satser och for loopar

Du får en datastruktur. Gör följande:

Extrahera en tuple med namn på alla aktiva studenter (de vars "aktiv"-status är True).

Skapa ett set med alla unika ämnen som de aktiva studenterna studerar.

Skapa en ordbok där nycklarna är kursnamnen och värdena är antalet aktiva studenter som är inskrivna i respektive kurs.

Skriv ut allt detta med print
"""

data = {
	"studenter": [
    	("Alice", {"ålder": 25, "ämnen": ("Matematik", "Fysik"), "aktiv": True}),
    	("Bob", {"ålder": 22, "ämnen": ("Biologi",), "aktiv": False}),
    	("Charlie", {"ålder": 23, "ämnen": ("Matematik", "Biologi"), "aktiv": True}),
    	("Diana", {"ålder": 24, "ämnen": ("Fysik",), "aktiv": False}),
    	("Eve", {"ålder": 21, "ämnen": ("Matematik", "Fysik", "Biologi"), "aktiv": True}),
	],
	"kurser": {
    	"Matematik": {"studenter": {"Alice", "Charlie", "Eve"}},
    	"Fysik": {"studenter": {"Alice", "Diana", "Eve"}},
    	"Biologi": {"studenter": {"Bob", "Charlie", "Eve"}},
	}
}

active_students = []
for student in data["studenter"]:
    name = student[0]
    details = student[1]
    if details["aktiv"]:
        active_students.append(name)

active_students_tuple = tuple(active_students)
print(active_students_tuple)

active_subjects = set()

for student in data["studenter"]:
    details = student[1]
    if details["aktiv"]:
        subjects = details["ämnen"]
        for subject in subjects:
            active_subjects.add(subject)

print(active_subjects)

# Skapa en ordbok där nycklarna är kursnamnen och värdena är antalet aktiva studenter som är inskrivna i respektive kurs.
active_per_course = {}
active_students_set = set(active_students)

for course_name, course_info in data["kurser"].items():
    course_students = course_info["studenter"]
    active_in_course = course_students.intersection(active_students_set)
    active = len(active_in_course)
    active_per_course[course_name] = active

print(active_per_course)





# student1 = data["studenter"][0]
# student2 = data["studenter"][1]
# student3 = data["studenter"][2]
# student4 = data["studenter"][3]
# student5 = data["studenter"][4]

# print(student1)
# print(student2)
# print(student3)
# print(student4)
# print(student5)

# subject1 = student1[1]["ämnen"]
# print(subject1)

