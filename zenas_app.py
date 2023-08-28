import streamlit
import snowflake.connector
import pandas

streamlit.header("Zena's Amazing Catalog")

#connector to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

#put data into dataframe
df = pandas.DataFrame(my_catalog)

#write dataframe to the page
streamlit.write(df)
