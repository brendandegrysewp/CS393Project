import pandas as pd
import html
import mysql.connector


print('##### Starting Data Cleaning #####')

# Read in CSV
df = pd.read_csv("aliensComplete.csv")


lenRows = len(df)
print(f'Number of Rows Before: {lenRows}')

# Drop unnecessary columns for duration in hours/min and column with random data (column 12)
df = df.drop('duration (hours/min)', axis = 1)
df = df.drop('Unnamed: 11', axis = 1)

# Remove single number values from Date_time
df = df[df['datetime'].str.contains('/', na=False)]

# Clean city, state, country - If none of them, drop entry
emptyLocation = df[(df['city'] == '') & (df['state'] == '') & (df['country'] == '')].index
df.drop(emptyLocation, inplace=True)

# Clean city - remove parenthesis
df['city'] = df['city'].str.split('(').str[0]

# Clean comments - HTML unescape
df['comments'] = df['comments'].fillna("Not Provided.")
df['comments'] = df['comments'].apply(html.unescape)

# Clean state - put not provided for city, state, country
df['city'] = df['city'].fillna("Not Provided.")
df['state'] = df['state'].fillna("Not Provided.")
df['country'] = df['country'].fillna("Not Provided.")

# Clean shape - put not provided for any not provided
df['shape'] = df['shape'].fillna("Not Provided.")

# Clean coords -  Any coord not as a float will be converted
df = df.replace('0', 0.0)
df = df.replace(0, 0.0)

# Clean coords - Find lat & long in same row both equal 0.0 and remove it
dfToDrop = df[(df['latitude'] == 0.0) & (df['longitude'] == 0.0)].index
df.drop(dfToDrop, inplace=True)

## Export to new csv
lenRows = len(df)
print(f'Number of Rows After: {lenRows}')
df.to_csv('cleanedAlienData.csv', index = False)
print('##### Export successful. New file named "cleanedAlienData.csv". #####')

conn = mysql.connector.MySQLConnection(
    host = '127.0.0.1',
    user = 'django',
    password = 'mysecretpassword',
    database = 'aliens'
)
cur = conn.cursor()

# for index, data in df.iterrows():
#     print(index,data)
#     break

for index, data in df.iterrows():
        date = data["datetime"].split("/")
        date = "-".join([date[2].split(" ")[0],date[0],date[1]]) + " " + date[2].split(" ")[1] + ":00"
        posted = data["date posted"].split("/")
        # print(index)
        if len(posted) != 3:
             continue
        try:
            posted = "-".join([posted[2],posted[0],posted[1]])
            # print(posted)
        except:
            posted = "0000-01-01"
        # print(index)
        try:
            cur.execute(""" insert into sighting (userId, date, city,state,country,shape,duration,comments,datePosted,latitude,longitude) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
            1,
            # index,
            date,
            data["city"],
            data["state"],
            data["country"],
            data["shape"],
            data["duration (seconds)"],
            data["comments"],
            posted,
            data["latitude"],
            data["longitude"],
            ))
        except:
            1

## Execute insert of data into database
conn.commit()