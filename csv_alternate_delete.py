import pandas as pd

df = pd.read_csv('numberplate.csv')

df = df.iloc[::2]

# writing into the file
df.to_csv("numberplate_final.csv", index=False)
  
print(df.to_string())

 
# computing number of columns
# rows = len(df.axes[0])
# print("number of rows : ", df.shape[0])
# print(rows)
# print(len(df.index))


# print(len(df))
# print(len(df.columns))