# Data Story #1 (truth) - Pie Chart
# %%
import pandas as pd
import altair as alt

df = pd.read_csv("gun_deaths.csv")

df['intent_clean'] = df['intent'].replace({
    'Accidental': 'Other',
    'Undetermined': 'Other'})

intent_counts = df['intent_clean'].value_counts().reset_index()
intent_counts.columns = ['intent', 'count']

intent_counts['percent'] = intent_counts['count'] / intent_counts['count'].sum() * 100

base = alt.Chart(intent_counts).encode(
    theta=alt.Theta("count:Q", stack=True),
    color=alt.Color("intent:N", title="Intent", scale=alt.Scale(scheme='category20')))

pie = base.mark_arc(outerRadius=120).properties(
    title="Distribution of Gun Death Intents", width=300, height=300)

labels = base.mark_text(
    radius=75,
    size=14,
    color=('white'),
    stroke='white',
    strokeWidth=1
).encode(
    text='percent_str:N'
).transform_calculate(
    percent_str="format(datum.percent, '.1f') + '%'"
)

truth_chart = pie + labels
truth_chart
# %%
