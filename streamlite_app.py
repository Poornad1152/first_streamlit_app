import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 &Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text("Hard-Boiled Free-Range Egg")
streamlit.text('Avocado Toast')

streamlit.header('Build your own Fruit Smoothie')

import pandas
my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruits_list = my_fruits_list.set_index('Fruit')

#Let's put a pick list here so they can pick the fruit hey want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruits_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruits_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)
