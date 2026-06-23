import pandas as pd
# loop = 0 

# while loop < 3:
#     loop += 1
#     print(f'Car is on loop {loop}')

# print(f'Car is off it has reached its destination {loop}')


# students = ['John', 'Jane', 'Jim', 'Jill']

df = pd.read_csv('imdb.csv')
while True: 
    user_movie = input('Search a movie you want: ')
    found = False
#     print(f'Student is {student}')

# print(f'All students have been printed')

#Using break and continue

    for movie in df['title']:
        if movie == user_movie:
            print(f'Your movie is found: {movie}')
            found = True
            break
    if not found:
        print(f"Your movie doesn't exist in this dataset")
        continue
    break


# while True:
#     try:
#         salary = int(input('Enter your salary: '))
#         print(f'Your salary is {salary}')
#         break
#     except ValueError:
#         print(f'Invalid input')
#         continue


