from pathlib import Path
import polars as pl
import plotly.express as px

cwd = Path.cwd()
csv_path = cwd / "sample_sales.csv"

df = pl.read_csv(csv_path)

fig = px.bar(
    df.to_pandas(),
    x="quarter",
    y="revenue",
    color="category",
    barmode="group",
    title="Quarterly Revenue by Category",
    labels={"quarter": "Quarter", "revenue": "Revenue ($K)", "category": "Category"},
)
fig.update_layout(template="plotly_white")

json_path = cwd / "sample_chart.json"
json_path.write_text(fig.to_json(), encoding="utf-8")
