# save_df_as_csv.py

import pandas as pd

raw_data = {
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
    'age': [42, 52, 36, 24, 73], 
    'pre_test_score': [4, 24, 31, 2, 3],
    'post_test_score': [25, 94, 57, 62, 70]
}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'pre_test_score', 'post_test_score'])
print(df)
df.to_csv("sample.csv")
