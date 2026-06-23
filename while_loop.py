
# loop = 0 

# while loop < 3:
#     loop += 1
#     print(f'Car is on loop {loop}')

# print(f'Car is off it has reached its destination {loop}')

students = ['John', 'Jane', 'Jim', 'Jill']

# for student in students:
#     print(f'Student is {student}')

# print(f'All students have been printed')

#Using break and continue

for student in students:
    print(f'Searching John...')
    if student == 'John':
        print(f'John found')
        break
    else:
        print(f'John not found')
        continue


