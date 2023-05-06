"""
From the given data we want to find what is average demograpohic of our students in the class.
1. What is the average age of the student in the class?
2. What percentage  of students are male and female?
3. What is the highest gpa in the class and what is the lowest gpa?
4. How many students are enrolled in the class?
Write the answers of above questions in a separate file.
Notes:
Make individual functions for each of the probelm when it makes sense.
Follow the general structure of code:
functions
main
 -- All the function call should happen here. Main should drive the flow of the program.
main function call
"""
import json


def read_from_file(input_file):
    with open(input_file, 'r') as file:
        data_file = file.read()
        json_file = json.loads(data_file)
        return json_file


def write_to_file(output_file, data):
    with open(output_file, 'w') as file:
        file.write(data)


def main():
    file_name = "students_data.json"
    file_name_2 = "average_demographics.txt"
    dict_library = read_from_file(file_name)
    average_age_list = []
    gender_list = []
    Males = []
    Females = []
    Max_list = []
    Min_list = []
    enrollment_list = []
    finalized_list = []
    for student_age in dict_library:
        total_age = student_age.get('age')
        average_age_list.append(total_age)
    total_amount = len(average_age_list)
    total_sum = sum(average_age_list)
    average_age = total_sum / total_amount  # Answer for number 1
    for gender_ratio in dict_library:
        total_gender = gender_ratio.get('gender')
        gender_list.append(total_gender)
    for gender in gender_list:
        if gender == 'Male':
            Males.append(gender)
        else:
            Females.append(gender)
    per_Male = (f"{len(Males) * 10}%")
    per_Female = (f"{len(Females) * 10}%")
    for total_gpa in dict_library:
        total_gender = total_gpa.get('age')
        Max_list.append(total_gender)
        Min_list.append(total_gender)
    maximum = Max_list[0]
    for value_Max in Max_list:
        if value_Max > maximum:
            maximum = value_Max
    minimum = Min_list[0]
    for value_Min in Min_list:
        if value_Min < minimum:
            minimum = value_Min
    # Answer for three
    for enrollment in dict_library:
        total_enrollments = enrollment.get('is_enrolled')
        enrollment_list.append(total_enrollments)
    for enrolled in enrollment_list:
        if enrolled is True:
            finalized_list.append(enrolled)
    students_enrolled = len(finalized_list)
    info = (f"The total average age for all students is {average_age}.\nPercetange of all males is {per_Male} and all females is {per_Female}.\nThe maximum gpa for all of the students is {maximum} and the minimium is {minimum}.\nTotal number of students that are enrolled in the class is {students_enrolled} students.")
    write_to_file(file_name_2, info)


main()
