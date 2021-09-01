student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = 0
for scores in student_scores:
    if scores > high_score:
      high_score = scores 
      
    
print(high_score)
    

    