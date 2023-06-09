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


def average_function_calculator(dict_age):
    average_age_list = []
    for student_age in dict_age:
        total_age = student_age.get('age')
        average_age_list.append(total_age)
    total_amount = len(average_age_list)
    total_sum = sum(average_age_list)
    average_age = total_sum / total_amount
    return average_age


def gender_ratio_calculator(dict_gender):
    malecount = 0
    femalecount = 0
    for gender_ratio in dict_gender:
        gender = gender_ratio.get('gender')
        if gender == 'Male':
            malecount = malecount + 1
        else:
            femalecount = femalecount + 1
    per_male = (f"{(malecount) * 10}%")
    per_female = (f"{(femalecount) * 10}%")
    return per_male, per_female


def gpa_value_calculator(dict_gpa):
    minimum = dict_gpa[0].get('gpa')
    maximum = dict_gpa[0].get('gpa')
    for total_gpa in dict_gpa:
        gpa = total_gpa.get('gpa')
        if gpa > maximum:
            maximum = gpa
        if gpa < minimum:
            minimum = gpa
    return maximum, minimum


def enrollment_checker(dict_enrolled):
    enrolled = dict_enrolled.get('is_enrolled')
    for enrollment in dict_enrolled:
        if enrolled is True:
            enrolled = enrollment
    print(enrolled)




def main():
    file_name = "students_data.json"
    file_name_2 = "average_demographics.txt"
    dict_library = read_from_file(file_name)
    average_age = average_function_calculator(dict_library)
    per_male, per_female = gender_ratio_calculator(dict_library)
    maximum, minimum = gpa_value_calculator(dict_library)
    enrollment_checker(dict_library)
    info = (f"The total average age for all students is {average_age}.\nPercetange of all males is {per_male} and all females is {per_female}.\nThe maximum gpa for all of the students is {maximum} and the minimium is {minimum}.\nTotal number of students that are enrolled in the class is students.")
    write_to_file(file_name_2, info)


main()
