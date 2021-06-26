import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import pandas as pd
from collections import defaultdict
import json

#url_data1 = (r'https://github.com/AnneDA/Recommender-app/blob/main/book_final_data.csv')
#book_final_data = pd.read_csv(url_data1, "x")
book_final_data = pd.read_csv(r'book_final_data.csv')


#url_data2 = (r'https://github.com/AnneDA/Recommender-app/blob/main/top_n.jsn')
#top_n = json.load(open(url_data2, "r"))
top_n = pd.read_csv(r'top_n.csv', "r")
                       



st.title('BOOK RECOMMENDER')

#create sidebar
st.sidebar.title("PLEASE SELECT YOUR USER PROFILE")

option = st.sidebar.selectbox(
    'USER PROFILES',book_final_data['user_id'].unique())

# User reading history
def get_history(userid):

        ratings = book_final_data.loc[book_final_data['user_id'] == (userid)]
        ratings=ratings[['book_title', 'rating']]
        if ratings.empty:
            print('Sorry your recommendation bucket is empty as you did not rate any books yet')
        else:
            df_reset=ratings.set_index('book_title')
            df_reset1=df_reset.sort_values(by='rating', ascending=False)
            return(df_reset1) 

# Recommender 
def get_reco_list(userid):
        reading_list = defaultdict(list)
        #top_n = get_top_n(predictions, n=5)
        for n in top_n[str(userid)]:
            book, rating = n
            title = book_final_data.loc[book_final_data.isbn==book].book_title.unique()[0]
            reading_list[title] = rating
            
        example_reading_list=reading_list.items()
        df= pd.DataFrame([(k,v) for k,v in example_reading_list], columns= ['book_title', 'rating'])
        df_set=df.set_index('book_title')
        df_set1=df_set.sort_values(by='rating', ascending= False).head(5)
                                   
        return(df_set1)
                                   
        return(df_set1)
    
if st.button('SHOW ME MY READING HISTORY!'):
    result = get_history (option)
    st.write('MY READING HISTORY:', result)
                                 
if st.button ("RECOMMEND ME 10 NEW BOOKS!"):
    result2 = get_reco_list (option)
    st.write('HERE WE GO, YOUR RECOMMENDATIONS:', result2)
            
   
