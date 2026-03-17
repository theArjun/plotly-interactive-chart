from pathlib import Path
import polars as pl
import plotly.express as px

cwd = Path.cwd()
csv_path = cwd / "sample_sales.csv"

# Read with Polars
# Parse date column for cleaner Plotly typing
df = pl.read_csv(csv_path, try_parse_dates=True)

# Build a sample Plotly chart
fig = px.line(
    df.to_pandas(),
    x="date",
    y="sales",
    color="category",
    markers=True,
    title="Sample Sales Over Time by Category",
)
fig.update_layout(template="plotly_white")

# Export chart JSON for Plotly.js
json_path = cwd / "sample_chart.json"
json_path.write_text(fig.to_json(), encoding="utf-8")
