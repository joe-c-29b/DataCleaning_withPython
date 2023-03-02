ff = [castaway_details, castaways, challenge_description, challenge_results, confessionals, hidden_idols, jury_votes, tribe_mapping, viewers, vote_history, season_summary, season_palettes, tribe_colours]
def lower_snake(df):
    colNames = []
    for col in df.columns:
        colNames.append(str.lower(col.replace(' ','_')))
    df.columns = colNames
for df in ff:
    lower_snake(df)