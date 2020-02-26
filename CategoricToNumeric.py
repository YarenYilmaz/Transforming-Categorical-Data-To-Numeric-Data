import pandas as pd

df = pd.read_csv('../categoric_data.csv')

# 1. REPLACING VALUES

# firstly, create a dictionary
replace_map = {
    "day": {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}}

# alternative dictionary creation if there is too many category to create by hand
labels = df["day"].astype('category').cat.categories.tolist()
replace_map_comp = {"day": {i: j for i, j in zip(labels, list(range(1, len(labels) + 1)))}}

df_1 = df.copy()
df_1.replace(replace_map, inplace=True)

# 2. LABEL ENCODING

df_2 = df.copy()
df_2["day"] = df_2["day"].astype("category")
df_2["day"] = df_2["day"].cat.codes

# 3. ONE-HOT ENCODING

df_3 = df.copy()
df_3 = pd.get_dummies(df_3, columns=["day"])

# 4. BINARY ENCODING

import category_encoders as ce
df_4 = df.copy()
encoder = ce.BinaryEncoder(cols=["day"])
df_4 = encoder.fit_transform(df_4)

# 5. BACKWARD DIFFERENCE ENCODING

df_5 = df.copy()
encoder = ce.BackwardDifferenceEncoder(cols=["day"])
df_5 = encoder.fit_transform(df_5)
