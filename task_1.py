# a program that check student range between 1,10 and adds whether the student failed or passed 


for students in range(1, 10):
    if students % 2 == 0:
        print('The student failed')
    elif students % 2 == 1:
        print('The student passed')