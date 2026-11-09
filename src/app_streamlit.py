import streamlit as st
import requests
import pandas as pd

st.title('STREAMLIT & API & SQL Project.')

option = st.sidebar.selectbox("Please choice menu:",
                              ('View all movies',
                              'View movie by id',
                              'View movie by title',
                              'Add new movie',
                              'Update movie',
                              'Delete movie'))

if option == 'View all movies':
    my_select = st.button("Click to view")
    if my_select:
        url = f"http://127.0.0.1:8000/getitem/"
        response = requests.get(url)
        if response.status_code != 200:
            st.success("Error Get URL!")

        else:
            result = response.json()
            df = pd.DataFrame(result)
            df = df.rename(columns={0: 'ID', 1: 'Movie_ID', 2: 'Title', 3: 'Poster',\
                                    4: 'Year', 5: 'Run_Time',\
                                    6: 'Country', 7: 'Rating', 8: 'Genres'})
            st.dataframe(df, column_config={
                                            'Poster': st.column_config.LinkColumn(
                                            'Poster', display_text='View Poster')},
                                            hide_index=True)
            
elif option == 'View movie by id':
    movie_id = st.number_input("Please enter movie id [1-249]: ", min_value=1, max_value=249)

    my_select = st.button("Click to view")
    if my_select:
        url = f'http://127.0.0.1:8000/getid/?movie_id={movie_id}'

        response = requests.get(url)
        if response.status_code != 200:
            st.success("Error Get URL!")

        else:
            data = response.json()
            df = st.table(data)

elif option == 'View movie by title':
    title = st.text_input("Please enter title movie: ")

    my_select = st.button("Click to view")
    if my_select:
        url = f'http://127.0.0.1:8000/gettitle/?title={title}'

        response = requests.get(url)
        if response.status_code != 200:
            st.success("Error Get URL!")

        else:
            data = response.json()
            df = st.table(data)
    

elif option == 'Add new movie':
    st.success("Please inpit new movie record:")
    cols_1 = st.columns(4)
    with cols_1[0]:
        movie_id = st.number_input('Movie ID: ')
    with cols_1[1]:
        title = st.text_input('Title: ').strip()
    with cols_1[2]:
        poster = st.text_input('Poster: ').strip()
    with cols_1[3]:
        year = st.number_input('Year: ')

    cols_2 = st.columns(4)
    with cols_2[0]:
        runtime = st.number_input('Run Time: ')
    with cols_2[1]:
        country = st.text_input('Country: ').strip().capitalize()
    with cols_2[2]:
        imdb_rating = st.number_input('Imdb Rating: ', format='%.1f')
    with cols_2[3]:
        genres = st.text_input('Genres: ').strip()

    my_select = st.button('Add Record')
    
    if my_select:
    #     try:
            #url = f"http://127.0.0.1:8000/add/?movie_id=3&title=3&poster=3&year=3&runtime=3&country=3&imdb_rating=3&genres=3
            url = f"http://127.0.0.1:8000/add/?movie_id={movie_id}&title={title}&poster={poster}&year={year}&runtime={runtime}&country={country}&imdb_rating={imdb_rating}&genres={genres}"
            
            response = requests.post(url)
            st.write(response.status_code)

                
            if response.status_code == 200:
                result = response.json()
                #st.write(result)
    
                if result.get('success'):
                    st.success(f"Movie added successfully! ID: {result.get('movie_id')}")
    #            else:
    #                st.error(f"Error: {result.get('error')}")
    #        else:
    #            st.error(f"Error: {response.status_code} - {response.text}")
    #
    #     except Exception as e:
    #        st.error(f"Connection Error: {str(e)}")            
    

elif option == 'Update movie':
    pass 

elif option == 'Delete movie':
    pass 
