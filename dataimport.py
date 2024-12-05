import pandas as pd
import html#https://www.educative.io/answers/what-is-htmlunescape-in-python
df = pd.read_csv("ufo_sighting_data.csv")
#df = df.fillna("Not Provided.")
#print(html.unescape(df.iat[43557,7]))
#Unescape everything in description and city
# Remove single number values from Date_time
