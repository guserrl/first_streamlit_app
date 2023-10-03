import streamlit
import snowflake.connector
import pandas
import requests
from urllib.error import URLError

streamlit.title('My Parents New Healty Dinner')

streamlit.header('🐔 Breakfast Menu')
streamlit.text('🥣 Croquetas')
streamlit.text('🥗 Tortilla patata')
streamlit.text('🍞 Canelones')
streamlit.text('🥑 Dani dame trabajo')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
print(fruits_selected)

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
#
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  #streamlit.write('The user entered ', fruit_choice)
  if not fruit_choice:
    streamlit.error('Seelct fruit')
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
  
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

# take json version of response and normalize it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output as a table
#streamlit.dataframe(fruityvice_normalized)

streamlit.stop();

#import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("Fruit load list")
streamlit.text(my_data_row)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)

#This not work
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
