from flask import Flask, render_template, request
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

app = Flask(__name__)

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('fooods.csv')

@app.route('/')
def index():
    # Display the head of the DataFrame
    head_html = df.head().to_html(classes='table table-striped')

    # Get column names
    columns = df.columns.tolist()

    return render_template('index.html', head_html=head_html, columns=columns)

@app.route('/visualize', methods=['POST'])
def visualize():
    column_name = 'Data.Protein'  # Visualizing specifically the 'Data.Protein' column

    # Generate bar chart
    bar_fig = px.bar(df, x=df.index, y=column_name, title=f'Bar Chart for {column_name}')
    bar_div = go.Figure(bar_fig).to_html(full_html=False)

    # Generate pie chart
    pie_fig = px.pie(df, values=column_name, names=df['Category'], title=f'Pie Chart for {column_name}')
    pie_div = go.Figure(pie_fig).to_html(full_html=False)

    # Generate box plot
    box_fig = px.box(df, x='Category', y=column_name, title=f'Box Plot for {column_name}')
    box_div = go.Figure(box_fig).to_html(full_html=False)

    # Generate scatter plot (protein vs. fat)
    scatter_fig = px.scatter(df, x='Data.Fat.Total Lipid', y=column_name, color='Category',
                             title=f'Scatter Plot: {column_name} vs. Fat Content')
    scatter_div = go.Figure(scatter_fig).to_html(full_html=False)

    return render_template('visualize.html', bar_div=bar_div, pie_div=pie_div,
                           box_div=box_div, scatter_div=scatter_div)

if __name__ == '__main__':
    app.run(debug=True)