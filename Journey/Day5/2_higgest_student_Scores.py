student_scores=[150, 142, 185, 120, 171, 186, 139, 182]

total_exam_score= sum(student_scores)
print(total_exam_score)

total=0
for score in student_scores:
    total +=score
print(total)


print(max(student_scores))
max_value=0
for score in student_scores:
    if score > max_value:
        max_value = score

print(max_value)