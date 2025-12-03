# Data Story #2 (trickery) - Horizontal Bar Chart
# %%
import pandas as pd
import altair as alt

df = pd.read_csv("gun_deaths.csv")

filtered_df = df[(df['place'] == 'Street') & (df['intent'].isin(['Suicide', 'Homicide']))]

intent_counts = (filtered_df.groupby('intent').size().reset_index(name='count'))

intent_counts['bar_size'] = intent_counts['intent'].map({'Homicide': 50,'Suicide': 53})

trickery_chart = alt.Chart(intent_counts).mark_bar().encode(
    x=alt.X('count:Q', title='Count', axis=alt.Axis(values=[0, 2000, 4000, 6000, 8000, 9000], ticks=True, grid = True, labelExpr="datum.value == 9000 ? '9000' : ''", labelPadding=4)),
    y=alt.Y('intent:N', sort='-x', title='Intent'),
    size=alt.Size('bar_size:Q', legend=None),
    color=alt.Color('intent:N', legend=None,
                    scale=alt.Scale(range=['steelblue', 'orange'])),
    tooltip=['intent:N', 'count:Q']
).properties(
    title='Leading Causes of Gun Deaths',
    width=400,
    height=150
)

trickery_chart
# %%
