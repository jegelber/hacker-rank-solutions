# Problem: https://www.hackerrank.com/challenges/grading/problem
# Score: 10/10

def gradingStudents(grades):
    ret = []
    for g in grades:
        if g < 38 or g%5 < 3:
            ret.append(g)
        else:
            if (g+1)%5 == 0:
                ret.append(g+1)
            else: # g+2 % 5 == 0
                ret.append(g+2)
    return ret
