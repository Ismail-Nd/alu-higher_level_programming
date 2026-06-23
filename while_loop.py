import pandas as pd
# loop = 0 

# while loop < 3:
#     loop += 1
#     print(f'Car is on loop {loop}')

# print(f'Car is off it has reached its destination {loop}')


# students = ['John', 'Jane', 'Jim', 'Jill']

df = pd.read_csv('labels.csv')
print(df.head())
print(df.columns)

#     print(f'Student is {student}')

# print(f'All students have been printed')

#Using break and continue

for name in df['image_name']:
    print(f'Searching  animal cat...')
    if name == 'caterpillar/4f787826ad.jpg':
        print(f'cat found')
        break
    else:
        print(f'cat not found')
        continue

# while True:
#     try:
#         salary = int(input('Enter your salary: '))
#         print(f'Your salary is {salary}')
#         break
#     except ValueError:
#         print(f'Invalid input')
#         continue


