#Milestone project 1

top_menu = "\n '1' -> to add a new movie, " \
              "\n '2' -> to see the movies on the list, " \
              "\n '3' -> to finde a movie by the title, " \
              "\n '4' -> to quite:  "
movie_list = []


def add_a_movie():
    title = input("Enter the movie title:")
    genere = input("Enter the movie genere:")
    year = input("Enter the movie year: ")
    director = input("Enter the movie director: ")

    movie_list.append({
        'title': title,
        'genere': genere,
        'year': year,
        'director': director
    })


def print_the_movie_list(movie):
    print({f"title: {movie['title']}", f"genere: {movie['genere']}", f"year: {movie['year']}", f"director: {movie['director']}"})


def list_movies():
    for movie in movie_list:
        print_the_movie_list(movie)


def search_for_movie():
    search_in_title = input("Enter movie title to search: ")
    for movie in movie_list:
        if movie["title"] == search_in_title:
            print_the_movie_list(movie)
        else:
            print("\n ! movie not in the list ! ")


def select_from_menu():
    user_selects = input(top_menu)
    while user_selects != '4':
        if user_selects == '1':
            add_a_movie()
        elif user_selects == '2':
            list_movies()
        elif user_selects == '3':
            search_for_movie()
        else:
            print("404, menu input not found")
        user_selects = input(top_menu)

select_from_menu()
