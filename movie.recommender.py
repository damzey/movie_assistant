import pprint

movies = [{'title': 'The Shawshank Redemption', 'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 'genre': 'Drama', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY67_CR0,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'}, {'title': 'The Godfather', 'description': 'The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son.', 'genre': 'Crime', 'image_url': 'https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY67_CR1,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0068646/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_2'}, {'title': 'The Dark Knight', 'description': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.', 'genre': 'Action', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY67_CR0,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0468569/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_3'}, {'title': 'The Godfather: Part II', 'description': 'The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.', 'genre': 'Crime', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMWMwMGQzZTItY2JlNC00OWZiLWIyMDctNDk2ZDQ2YjRjMWQ0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY67_CR1,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0071562/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_4'}, {'title': '12 Angry Men', 'description': 'The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.', 'genre': 'Crime', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhNGUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_UX45_CR0,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0050083/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_5'}]


def get_unique_genres():
    genre_choices = []
    for movie in movies:
        genre_choices.append(movie['genre'])
    genre_list = []
    for genre in genre_choices:
        if genre not in genre_list:
            genre_list.append(genre)
    genre_choice = input(f"What genre do you want out of {genre_list} ? ").capitalize()
    return genre_choice

def get_movies_in_genre(genre_choice):
    for movie in movies:
        if movie['genre'] == genre_choice:
            print(movie['title'])

def get_movies_in_genre(genre_choice):
    movies_returned = []
    for movie in movies:
        if movie['genre'] == genre_choice:
            movies_returned.append(movie['title'])
    print(movies_returned)

def pick_a_movie():
    print()
    movie_choice = input('What movie do you want to pick? (please type the full movie name) ').title()
    for movie in movies:
        if movie['title'] == movie_choice:
            pprint.pprint(movie)

def pick_genre_movie_and_display_details():
    genre_choice = get_unique_genres()
    get_movies_in_genre(genre_choice)
    pick_a_movie()

pick_genre_movie_and_display_details()