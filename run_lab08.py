from src.lab08.serialize import students_from_json, students_to_json
from src.lab08.models import Student

def main():
    students = students_from_json("data/lab08/students_input.json")
    for s in students:
        print(s, "Возраст:", s.age())
    students.append(Student("Сидоров С.", "2000-01-10", "SE-02", 4.9))
    students_to_json(students, "data/lab08/students_output.json")
    print("Saved", len(students), "students to data/lab08/students_output.json")

if __name__ == "__main__":
    main()