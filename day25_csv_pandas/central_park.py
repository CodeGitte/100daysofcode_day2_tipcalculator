#import relevant libraries 
import pandas as pd

#read the squirrel data 
data = pd.read_csv("central_park.csv")

#create new dataframe withe the primary fur color, and frequency 
new_df = data.groupby("Primary Fur Color").count()
new_df = new_df.X
new_df = new_df.reset_index()
new_df = new_df.rename(columns = {"X" : "Frequency"})
print(new_df)