import pandas as pd
Quotes=[]
genre='gratitude'
df=pd.read_csv('Info.csv')
for index,rows in df.iterrows():
    if genre in rows['category']:
        Quotes.append(rows['quote'])
        
print(Quotes)
   