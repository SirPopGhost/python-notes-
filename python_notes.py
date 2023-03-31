'''
Homework:
1. Create 3 dictionary which contains information of those 3 students.
2. Find the max score in Math, physics, and checmistry and SAT for all the students.

Bonus:
Find out of all these 3 students which student had the higehst in each of of subject.
'''
Bob = {
    "name": "Bob",
    "grade": 11,
    "isMale": True,
    "SAT": [90, 45, 99, 100, 87],
    "subject_specific_scores": {
        "math": [100, 100, 100, 99, 98],
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
        "math": [90, 95, 98, 96, 95],
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
        "math": [77, 76, 81, 84, 81],
        "physics": [45, 56, 58, 39, 41],
        "chemistry": [21, 23, 35, 44, 31]
    }
}


def student_data(subject_score_dictionary, subject):
    print(max(subject_score_dictionary.get(subject)), " ", subject)


student_data(Matt.get("subject_specific_scores"), "math")
student_data(Zach.get("subject_specific_scores"), "physics")


# subject_specific_scores_Bob = Bob.get("subject_specific_scores")
# subject_specific_scores_Matt = (Matt.get("subject_specific_scores")).get("math")
# subject_specific_scores_Zach = Zach.get("subject_specific_scores")

# print(max(subject_specific_scores_Bob.get('math')))
# print(subject_specific_scores_Matt)

# total = []

# total.append(subject_specific_scores_Bob.get("math"))

# total.append(subject_specific_scores_Zach.get("math"))

# print(total)
