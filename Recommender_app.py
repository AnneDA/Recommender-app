import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import pandas as pd
from collections import defaultdict
import json

book_final_data = pd.read_csv(r"C:\Users\Annekathrin\Desktop\york\Course 5\Project 1/book_final_data.csv")
top_n = json.load(open(r"C:\Users\Annekathrin\Desktop\york\Course 5\Project 1/top_n.jsn", "r"))


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
        return(reading_list)
    
if st.button('SHOW ME MY READING HISTORY!'):
    result = get_history (option)
    st.write('MY READING HISTORY:', result)
                                 
if st.button ("RECOMMEND ME 10 NEW BOOKS!"):
    result2 = get_reco_list (option)
    st.write('HERE WE GO, YOUR RECOMMENDATIONS:', result2)
            
   
