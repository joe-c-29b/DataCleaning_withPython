def val_cou(df):
    for col in df.columns:
        print(df[col].value_counts())
val_cou(house_cats)