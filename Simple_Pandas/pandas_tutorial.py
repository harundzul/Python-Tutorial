import pandas as pd

data = {'Name': ['Ali', 'Abu', 'Meow', 'Gong'],
        'Age': [33, 62, 51, 42],
        'Qualification': ['Msc', 'MBA', 'Msc', 'Msc']}

address = {'Penang': 'Ali', 'Selangor': 'Abu',
           'Sabah': 'Meow', 'Sarawak': 'Gong'}

df = pd.DataFrame(data)

print(df)

df['Address'] = address
  
print(df)

