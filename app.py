import streamlit as st
import pandas as pd

# Introduction
def introduction():
    st.title('Streamlit Cookbook')
    st.write('Welcome to the Streamlit Cookbook! Choose a section from the sidebar to view code snippets.')
    
def custom_metric(label, value, delta1, delta2):
    # Determine arrow direction for delta1
    arrow1 = "&#8593;" if "+" in delta1 else "&#8595;"
    # Determine arrow direction for delta2
    arrow2 = "&#8593;" if "+" in delta2 else "&#8595;"
    
    metric_html = f"""
    <div class="metric-container">
        <span class="metric-label">{label}</span><br>
        <span class="metric-value">{value}</span><br>
        <span class="metric-delta1">{arrow1} {delta1}</span><br>
        <span class="metric-delta2">{arrow2} {delta2}</span>
    </div>
    """
    return metric_html

def render_metrics(*metrics):
    # Combining the individual metric HTML into a flexbox container
    combined_html = f"""
    <style>
        .metrics-flex-container {{
            display: flex;
            justify-content: space-around;  /* Equally spaced items */
            flex-wrap: wrap;  /* Allow wrapping to next line if needed */
        }}
        .metric-container {{
            flex: 1;  /* Allow items to grow and shrink */
            margin: 10px;
            min-width: 200px;  /* Set a minimum width for items */
        }}
        .metric-label {{ font-size: 16px; color: gray; }}
        .metric-value {{ font-size: 24px; }}
        .metric-delta1 {{ color: red; }}
        .metric-delta2 {{ color: green; }}
    </style>
    <div class="metrics-flex-container">
        {''.join(metrics)}
    </div>
    """
    st.markdown(combined_html, unsafe_allow_html=True)



# Data Tables
def data_tables():
    st.title('Data Tables')
    sample_data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['NY', 'SF', 'LA']
    }
    df = pd.DataFrame(sample_data)
    st.write(df)
    code = """
sample_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NY', 'SF', 'LA']
}
df = pd.DataFrame(sample_data)
st.write(df)
    """
    st.code(code, language='python')

# Plots
def plots():
    st.title('Plots')
    sample_data = {
        'Year': [2020, 2021, 2022],
        'Sales': [100, 150, 200]
    }
    df = pd.DataFrame(sample_data)
    st.line_chart(df.set_index('Year'))
    st.bar_chart(df.set_index('Year'))
    code = """
sample_data = {
    'Year': [2020, 2021, 2022],
    'Sales': [100, 150, 200]
}
df = pd.DataFrame(sample_data)
st.line_chart(df.set_index('Year'))
st.bar_chart(df.set_index('Year'))
    """
    st.code(code, language='python')

# Filters
def filters():
    st.title('Filters')
    selected_value = st.slider('Select a value:', 0, 100, 50)
    st.write(f'You selected: {selected_value}')
    options = ['Option A', 'Option B', 'Option C']
    selected_option = st.selectbox('Choose an option:', options)
    st.write(f'You selected: {selected_option}')
    code = """
selected_value = st.slider('Select a value:', 0, 100, 50)
options = ['Option A', 'Option B', 'Option C']
selected_option = st.selectbox('Choose an option:', options)
    """
    st.code(code, language='python')

# Interactivity
def interactivity():
    st.title('Interactivity')
    if st.button('Say Hello'):
        st.write('Hello, Streamlit!')
    user_input = st.text_input('Enter something:')
    st.write(f'You wrote: {user_input}')
    code = """
if st.button('Say Hello'):
    st.write('Hello, Streamlit!')
user_input = st.text_input('Enter something:')
    """
    st.code(code, language='python')

# Merged Recipe: Data Tables, Plots, and Filters
def merged_recipe():
    st.title('Merged Recipe: Data Tables, Plots, and Filters')
    data = {
        'Year': [2019, 2020, 2021, 2022],
        'Sales': [100, 150, 200, 250],
        'Region': ['North', 'South', 'East', 'West']
    }
    df = pd.DataFrame(data)
    year_range = st.sidebar.slider('Select Year Range', min_value=2019, max_value=2022, value=(2019, 2022))
    filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
    regions = ['All'] + list(df['Region'].unique())
    selected_region = st.sidebar.selectbox('Select Region', regions)
    if selected_region != 'All':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    st.subheader('Data Table')
    st.write(filtered_df)
    st.subheader('Sales Plot')
    st.line_chart(filtered_df.set_index('Year')['Sales'])
    code = """
# Sample data and filtering code from above
    """
    st.code(code, language='python')
    
 
def custom_metrics_display():
    st.title('Custom Metrics Display')
    metric1 = custom_metric("Sales", "1000", "+10 from last week", "-15 from last month")
    metric2 = custom_metric("Revenue", "5000", "+20 from last week", "-5 from last month")
    metric3 = custom_metric("Profit", "500", "+5 from last week", "+10 from last month")
    render_metrics(metric1, metric2, metric3)

    code = """
# Code for the custom_metric function and its usage
    """
    st.code(code, language='python')
 

# Sidebar and main flow
st.sidebar.title('Navigation')
selection = st.sidebar.radio(
    "Go to", 
    ['Introduction', 'Data Tables', 'Plots', 'Filters', 'Interactivity', 'Merged Recipe', 'Custom Metrics Display']
)

if selection == 'Introduction':
    introduction()
elif selection == 'Data Tables':
    data_tables()
elif selection == 'Plots':
    plots()
elif selection == 'Filters':
    filters()
elif selection == 'Interactivity':
    interactivity()
elif selection == 'Merged Recipe':
    merged_recipe()
elif selection == 'Custom Metrics Display':
    custom_metrics_display()