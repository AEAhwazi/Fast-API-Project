import sqlite3

DBNAME = 'MyDatabase.db'

def fun_view_all():    
    conn = sqlite3.connect(DBNAME)    
    cursor = conn.cursor()
    quary = '''SELECT * FROM movie'''
    rows = cursor.execute(quary).fetchall()
    conn.close()
    return rows

def fun_view_id(movie_id):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    quary = '''
            SELECT * FROM movie WHERE movie_id = ?'''

    rows = cursor.execute(quary, (movie_id,)).fetchone()
    conn.close()
    return rows

def fun_view_title(title):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    quary = '''
            SELECT * FROM movie WHERE title = ?'''

    rows = cursor.execute(quary, (title,)).fetchone()
    conn.close()
    return rows

def fun_add_record(movie_id, title, poster, year,
                    runtime, country, imdb_rating, genres):

        conn = sqlite3.connect(DBNAME)

        cursor = conn.cursor()
        query = '''
                INSERT INTO movie(movie_id, title, poster,
                  year, runtime, country, imdb_rating, genres)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?)
                '''
        try:
             cursor.execute(query, (movie_id, title, poster, year,
                                     runtime, country, imdb_rating, genres))
        
             conn.commit()

             result = {"success": True, "inserted": cursor.rowcount, "movie_id": movie_id}

        except Exception as e:
                result = {"success": False, "error": str(e)}

        finally:
              conn.close()
    
        return result
    
#data = fun_view_id(1)
#data = fun_view_title('The Godfather')
#result = fun_add_record()
#print(result)

#print(data)


    


#END PROGRAM.
