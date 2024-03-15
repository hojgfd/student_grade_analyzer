#CHATGPT: Lav en "student analyzer" der analyserer elevers karakterer med gennemsnit, højeste og laveste karakter.

studentAmount = input("Enter number of students")

studentNames = []
studentGrades = []
studentGradeAmounts = []


for i in range(int(studentAmount)):
    name = input("Enter student " + str(i+1) + " name")
    studentNames.append(name)
    grades = []
    grades = input("Enter grades in percentage seperated by comma: ")
    studentGrades.append(grades)
    studentGradeAmounts.append(len(grades))

for i in range(len(studentNames)):
    print("Analysis:")
    print("Student: " + studentNames[i])
    averageGrade = 0
    for ii in range(len(grades)):
        if ii == studentGradeAmounts[i]:
            print("unfinished GG")

        print("Average grade: ")




