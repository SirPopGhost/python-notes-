Bob = {
    "name": "Bob",
    "grade": 11,
    "isMale": True,
    "SAT": [90, 45, 99, 100, 87],
    "subject_specific_scores": {
        "math": [99, 100, 100, 99, 98],
        "physics": [0, 78, 90, 50, 94],
        "chemistry": [99, 100, 78, 99, 80]
    }
}

Matt = {
    "name": "Matt",
    "grade": 10,
    "isMale": True,
    "SAT": [90, 98, 75, 85, 87],
    "subject_specific_scores": {
        "math": [99, 76, 55, 96, 95],
        "physics": [87, 89, 77, 86, 89],
        "chemistry": [80, 95, 87, 89, 91, 100]
    }
}

Zach = {
    "name": "Zach",
    "grade": 12,
    "isMale": True,
    "SAT": [50, 60, 55, 54, 43],
    "subject_specific_scores": {
        "math": [77, 74, 81, 84, 81],
        "physics": [45, 56, 58, 39, 41],
        "chemistry": [21, 23, 35, 44, 31]
    }
}


def student_data(student_info, subject):
    student_name = student_info.get("name")
    sub_min = student_info.get("subject_specific_scores")
    minimum = min(sub_min.get(subject))
    return {
        "name": student_name,
        "min": minimum
    }


#    print(min(student_info.get(subject)), " ", subject)
bob_min = student_data(Bob, "math")
matt_min = student_data(Matt, "math")
zach_min = student_data(Zach, "math")

epic_list = [bob_min, matt_min, zach_min]


def minimum_dictonaries_math(math_min: list):
    mint = math_min[0]
    for value in math_min:
        if value.get("min") < mint.get("min"):
            mint = value
    return mint


print(minimum_dictonaries_math(epic_list))
