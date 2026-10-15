import requests

base = "http://localhost:3000"


def createStudent(data):
    response = requests.post(f"{base}/students", data)
    if response == 201:
        print(response.json())
    else:
        error = response.json()
        print(error)

def get_student(id):
    response = requests.get(f"{base}/students/{id}")

    if response.status_code == (200, 201):
        print(response.json())
    else:
        error = response.json()
        print(error)

def get_students():
    response = requests.get(f"{base}/students")

    if response == 200:
        print(response.json())
    else:
        error = response.json()
        print(error)

def deleteStudent(id):
    response = requests.delete(f"{base}/students/{id}")

    if response.status_code == (200, 204):
        print("Student Deleted Successflly")
    else:
        error = response.json()
        print(f"{error}", "Student Failed to be deleted")


print(createStudent({"name": "Promis", "Year": "J25"}))
# print(get_students())
print(get_student("a6a239b1-e81a-429a-a9b4-90615bd433df"))
# print(deleteStudent("cd388c8f-5052-4e31-8155-15c47396c6a6"))