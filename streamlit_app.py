import streamlit

streamlit.title('My Parents New Healty Dinner')

streamlit.header('🐔 Breakfast Menu')
streamlit.text('🥣 Croquetas')
streamlit.text('🥗 Tortilla patata')
streamlit.text('🍞 Canelones')
streamlit.text('🥑 Dani dame trabajo')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
