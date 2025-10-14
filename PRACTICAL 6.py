#PRACTICAL 6
#Q1

def count_occurrences(n):
    counts = [0] * 4
    for _ in range(n):
        num = int(input("Enter a number between 0 and 3: "))
        if num >= 0 and num <= 3:
            counts[num] += 1
    for i, count in enumerate(counts):
        print(f"Number {i} occurred {count} times.")

#Q2
        
def calculate_average(n):
    values = tuple(float(input("Enter a numeric value: ")) for _ in range(n))
    avg = sum(values) / n
    print(f"The average of the values is: {avg}")

#Q3
    
def find_runner_up_score(scores):
    unique_scores = sorted(set(scores), reverse=True)
    runner_up_score = unique_scores[1]
    print(f"The runner-up score is: {runner_up_score}")

#Q4
def process_students(n):
    students = {}
    for i in range(n):
        name = input("Enter student name: ")
        city = input("Enter city: ")
        students[name] = city

    # a) Display all names
    print("All names:", list(students.keys()))

    # b) Display all city names
    print("All city names:", list(set(students.values())))

    # c) Display student name and city of all students
    print("Student names and cities:")
    for name, city in students.items():
        print(f"{name}: {city}")

    # d) Count number of students in each city
    city_counts = {}
    for city in students.values():
        city_counts[city] = city_counts.get(city, 0) + 1
    print("Number of students in each city:")
    for city, count in city_counts.items():
        print(f"{city}: {count}")

#Q5
        
def process_movies(n):
    movies = []
    for _ in range(n):
        name = input("Enter movie name: ")
        year = int(input("Enter year of release: "))
        director = input("Enter director name: ")
        production_cost = float(input("Enter production cost: "))
        collection = float(input("Enter collection made: "))
        movies.append({"name": name, "year": year, "director": director, "production_cost": production_cost, "collection": collection})

    # a) Print all movie details
    print("All movie details:")
    for movie in movies:
        print(movie)

    # b) Display name of movies released before 2015
    print("Movies released before 2015:")
    for movie in movies:
        if movie['year'] < 2015:
            print(movie['name'])

    # c) Print movies that made a profit
    print("Movies that made a profit:")
    for movie in movies:
        if movie['collection'] > movie['production_cost']:
            print(movie['name'])

    # d) Print movies directed by a particular director
    director_name = input("Enter director name to filter movies: ")
    print(f"Movies directed by {director_name}:")
    for movie in movies:
        if movie['director'] == director_name:
            print(movie['name'])

