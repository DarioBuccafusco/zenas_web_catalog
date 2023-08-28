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
#streamlit.write(df)

color_list = df[0].values.tolist()
#streamlit.write(color_list)

option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

# We'll build the image caption now, since we can
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option + "';")

df2 = my_cur.fetchone()

streamlit.write(df2)
