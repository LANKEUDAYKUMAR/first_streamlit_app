import streamlit
streamlit.title('my moms new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣omega 3, blueberry oatmeal')
streamlit.text('🥗kale, spinach & rocket smoothe')
streamlit.text(' 🐔 hard-boiled free range egg')
streamlit.text('🥑 Avacado toast') 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.dataframe(my_fruit_list)
fruits_selected =streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Banana','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())





