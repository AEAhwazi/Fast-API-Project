'''
Programming: Python / FastAPI
Author     : AEAhwazi
Date       : 2026/09/21
Project    : Create API
'''

from fastapi_offline import FastAPIOffline  # Import FastAPI
import app_query_movies                     # Import App Sqlite3 / Database / Quary

my_list = [1, 2, 3, 4, 5]

app = FastAPIOffline()

@app.get('/')
def get_index():                            # Function Index '/'
    return('Hello World!')

@app.get('/home')                           # Function Home
def get_home():
    return('Hello Home')

@app.get('/getitem/')                       # Function Get all recrods from Table Movie
def get_item():
    data = app_query_movies.fun_view_all()
    return(data)

@app.get('/getid/')                                    # Function Get one record by Movie ID
def get_id(movie_id):
    data = app_query_movies.fun_view_id(movie_id)
    return(data)

@app.get('/gettitle/')                                 # Function Get one record by Movie Title
def get_title(title):
    data = app_query_movies.fun_view_title(title)
    return(data)

@app.post('/add/')                           # Function Add new record to Table Movie
def post_new_item(movie_id: int, title: str,\
                   poster: str = "", year: int = 0,\
                      runtime: int = 0, country: str = "",\
                          imdb_rating: float = 0.0, genres: str = ""):

    result = app_query_movies.fun_add_record(movie_id, title, poster, year,
                                              runtime, country, imdb_rating, genres)
    return {'Result': result}

@app.post('/addindex/')
def post_add_index(index:int, new_item:int):
    if index < len(my_list):
        my_list.insert(index, new_item)
        return(my_list)

    else:
        return('Error!, Out off index')

@app.delete('/deleteitam/')
def delete_delete_item(item:int):
    if item in my_list:
        my_list.remove(item)
        return(my_list)

    else:
        return('Error!, Item Not Found!')

@app.delete('/deleteindex/')
def delete_delete_item(index:int):
    if index <= len(my_list):
        my_list.pop(index)

        return(my_list)

    else:
        return('Error!, Item Not Found, [Out off Index]!')

@app.put('/updateitem/')
def put_update_item(olditem:int, newitem:int):
    if olditem in (my_list):

        index = my_list.index(olditem)
        my_list[index] = newitem

        return(my_list)

    else:
        return('Error!, Item Not Found, [Out off Index]!')

@app.put('/updateindex/')
def put_update_index(index:int, newitem:int):
    if index <= len(my_list):

        my_list[index] = newitem

        return(my_list)

    else:
        return('Error!, Item Not Found, [Out off Index]!')

#END PROGRAM.
