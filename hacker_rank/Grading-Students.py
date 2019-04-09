def gradingStudents(grades, base=5):
    grades_results = []
    grades_final = []
    for b in grades:
        print(b, b % base)
        if b % base == 3:
            val = b + 2
            grades_results.append(val)
            print(val)
        elif b % base == 1:
            val = b + 4
            grades_results.append(val)
            print(val)
        else:
            val = int(round((b + 1) / 5.0) * 5.0)
            grades_results.append(val)
            print(val)


    for i, b in enumerate(grades):
        print(i, b, grades_results[i] - b, grades_results[i])
        if grades_results[i]-b < 3 and b >= 38:
            grades_final.append(grades_results[i])
        if grades_results[i]-b == 3 or b < 38:
            grades_final.append(b)
        if grades_results[i]-b == 4 and b >= 38:
            grades_final.append(b)

    return (grades_results, grades_final)



    # grades_results = []
    # grades_final = []
    # for _ in grades:
    #     grade = int(base * round(float(_) / base))
    #     grades_results.append(grade)
    #
    # for i, grade in enumerate(grades_results):
    #     print(grade - grades[i])
    #     print(grade, grades[i])
    #     if grade - grades[i] < 3: grades_final.append(grade)
    #     if grade - grades[i] == 3: grades_final.append(grades[i])
    #
    # return grades_final

grades = [
    73,
    67,
    38,
    33
]

grades1 = [
    23,
    80,
    96,
    18,
    73,
    78,
    60,
    60,
    15,
    45,
    15,
    10,
    5,
    46,
    87,
    33,
    60,
    14,
    71,
    65,
    2,
    5,
    97,
    0
]
print(gradingStudents(grades))
