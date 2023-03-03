def val_cou(df):
    for col in df.columns:
        print(df[col].value_counts())
val_cou(house_cats)

##alternate to output the total value count next to the column name
def val_cou(df):
    for col in df.columns:
        print(df[col].value_counts().sum(), col)
val_cou(house_cats)
