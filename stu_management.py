import json
import os
import string
import random
from pathlib import Path

class Students:
    data = []
    database = "student.json"

    try:
        # Load data from the existing JSON file if it exists
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
    except Exception as err:
        print(err)

    @classmethod
    def UpdateStudent(cls):
        # Update the JSON file with the latest data
        with open(cls.database, "w") as fs:
            fs.write(json.dumps(cls.data))
        print("Updated successfully")

    @classmethod
    def randomid(cls):
        # Generate a random ID for a student
        alpha = random.choices(string.ascii_letters, k=3)
        numbers = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=2)
        id = alpha + numbers + spchar
        random.shuffle(id)
        return "".join(id)

    @classmethod
    def register_student(cls):
        # Register a new student
        json_file_path = cls.database

        if not os.path.exists(json_file_path):
            # If the file doesn't exist, create it with an empty list
            with open(json_file_path, 'w') as file:
                json.dump([], file)

        # Get student details from the user
        stu = {
            "id": cls.randomid(),
            "name": input("Tell your name: "),
            "email": input("Tell your email: "),
            "password": input("Tell your password: "),
            "skill": input("Tell your skill: ")
        }

        # Load existing data from the JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        # Add the new student data to the list
        data.append(stu)

        # Update the JSON file with the new data
        with open(json_file_path, 'w') as file:
            json.dump(data, file)

        print("Registered successfully")

    def readsinglestudent(self):
        # Read details of a single student based on ID and password
        id = input("Enter ID: ")
        password = input("Enter Password: ")
        student = [i for i in Students.data if i["id"] == id and i["password"] == password]

        if not student:
            print("Invalid credentials or student not found.")
        else:
            print("Student Details:")
            for key, value in student[0].items():
                print(f"{key}: {value}")

    def accessdata(self):
        # Access details of all students in the database
        a = Students.data
        counter = 1
        for i in a:
            print()
            print(f"Student {counter}")
            print()
            for j in i:
                print(f"{j} : {i[j]}")
            counter += 1

    def UpdateStudentdata(self):
        # Update details of an existing student
        id = input("Enter Id: ")
        password = input("Enter Password: ")
        student = [i for i in Students.data if i["id"] == id and i["password"] == password]
        if len(student) == 0:
            print("Invalid credentials")
        else:
            print("Enter to skip")
            stu = {
                "name": input("Please tell your new name: "),
                "email": input("Please tell your new email: "),
                "password": input("Tell your password: "),
                "skill": input("Update your skill: ")
            }
            
            if stu["name"] == "":
                stu["name"] = student[0]["name"]
            if stu["email"] == "":
                stu["email"] = student[0]["email"]
            if stu["password"] == "":
                stu["password"] = student[0]["password"]
            if stu["skill"] == "":
                stu["skill"] = student[0]["skill"]

            for i in stu.keys():
                if stu[i] == student[0][i]:
                    continue
                else:
                    student[0][i] = stu[i]
            self.UpdateStudent()
            print("Update successfully")

    def deletestudent(self):
        # Delete a student based on ID and password
        id = input("Tell the ID: ")
        password = input("Enter the password: ")
        student = [
            i 
            for i in Students.data
            if i["id"] == id and i["password"] == password
        ]

        if len(student) == 0:
            print("Invalid credentials")
        else:
            check = input("Are you sure to delete it? Press Y/N")

            if check == "Y" or check == "y":
                studentindex = Students.data.index(student[0])
                Students.data.pop(studentindex)
                self.UpdateStudent()
                print("Deleted successfully")
            
            elif check == "N" or check == "n":
                pass

            else:
                print("Wrong input")

# Create an instance of the Students class
randomname = Students()

# Main program loop
while True:     
    print("""
    Select an option:
        1: Register a student
        2: Login student profile
        3: Access database
        4: Update Student data
        5: Delete student
        0: Exit the application
    """)
    n = int(input("Tell your response: "))

    if n == 0:
        exit(0)

    if n == 1:
        randomname.register_student()

    if n == 2:
        randomname.readsinglestudent()

    if n == 3:
        randomname.accessdata()

    if n == 4:
        randomname.UpdateStudentdata()

    if n == 5:
        randomname.deletestudent()
