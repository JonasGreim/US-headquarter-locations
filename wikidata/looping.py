import os
import pandas as pd


current_dir = os.path.dirname(__file__)
# parent_dir_path = os.path.join(current_dir, ".")
file_path = os.path.join(current_dir, "50items.json")

df = pd.read_json(file_path, orient='columns')
filtered_data = df.loc[df['rank'] <= 50]
count = filtered_data['company'].unique()

for i in count:
    print(i)

# print('heluuuuu ', len(count))