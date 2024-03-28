def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade >= 38:
            next_multiple_of_five = grade + (5 - grade % 5)
            if next_multiple_of_five - grade < 3:
                rounded_grades.append(next_multiple_of_five)
            else:
                rounded_grades.append(grade)
        else:
            rounded_grades.append(grade)
    return rounded_grades

#Julia
function gradingStudents(grades)
    rounded_grades = Int[]
    for grade in grades
        # Check if the grade is greater than or equal to 38
        if grade >= 38
            # Calculate the next multiple of 5
            next_multiple_of_five = grade + (5 - grade % 5)
            
            # Check if the difference is less than 3
            if next_multiple_of_five - grade < 3
                # Round up to the next multiple of 5
                push!(rounded_grades, next_multiple_of_five)
            else
                # Keep the grade as is
                push!(rounded_grades, grade)
            end
        else
            # If the grade is less than 38, just append it
            push!(rounded_grades, grade)
        end
    end
    return rounded_grades
end
