import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
import ipywidgets as widgets
from IPython.display import display, clear_output

# ---- Set Plot Style ----
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (8,5)

# ---- Step 1: Upload CSV ----
print("📂 Please upload your YouTube stats CSV file (e.g., youtube_stats.csv)")
print("Columns should include: Month, Views, Likes, Watch_Hours\n")

uploaded = files.upload()

# ---- Step 2: Load and Display Data ----
for file_name in uploaded.keys():
    df = pd.read_csv(file_name)

display(df.head())
print("\n✅ Dataset Loaded Successfully!")

# ---- Step 3: Dropdown for Metric Selection ----
metric_dropdown = widgets.Dropdown(
    options=[col for col in df.columns if col != "Month"],
    description='Metric:',
    style={'description_width': 'initial'},
)

# ---- Step 4: Dropdown for Graph Type ----
graph_dropdown = widgets.Dropdown(
    options=['Line Chart', 'Bar Chart', 'Seaborn Style'],
    description='Graph Type:',
    style={'description_width': 'initial'},
)

# ---- Step 5: Plot Button ----
plot_button = widgets.Button(
    description="📊 Show Graph",
    button_style='success',
    tooltip='Click to visualize data'
)

output = widgets.Output()

# ---- Step 6: Define Visualization Function ----
def visualize_data(b):
    with output:
        clear_output(wait=True)
        metric = metric_dropdown.value
        graph_type = graph_dropdown.value

        if graph_type == "Line Chart":
            plt.plot(df["Month"], df[metric], marker='o', color='royalblue', linewidth=2)
        elif graph_type == "Bar Chart":
            plt.bar(df["Month"], df[metric], color='skyblue', edgecolor='black')
        elif graph_type == "Seaborn Style":
            sns.lineplot(x="Month", y=metric, data=df, marker='o', color='coral')

        plt.title(f"YouTube Channel {metric} Growth", fontsize=14, fontweight='bold')
        plt.xlabel("Month")
        plt.ylabel(metric)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

        # Summary Stats
        print(f"\n📈 Summary for {metric}:")
        print(df[metric].describe())

# ---- Step 7: Bind Button ----
plot_button.on_click(visualize_data)

# ---- Step 8: Display Interactive Widgets ----
display(widgets.VBox([metric_dropdown, graph_dropdown, plot_button, output]))
