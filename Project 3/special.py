import pandas as pd
import plotly.express as px

def load_and_clean_data(filepath):
    # Load data, assuming the correct headers are from the first row now
    df = pd.read_csv(filepath, skiprows=1)
    # Ensure we know what the columns are named after loading
    print("Columns after loading:", df.columns.tolist())
    
    # Assuming correct column names are 'Country', 'Country Code', 'Indicator Name', 'Indicator Code'
    df.rename(columns={df.columns[0]: 'Country', df.columns[1]: 'Country Code',
                       df.columns[2]: 'Indicator Name', df.columns[3]: 'Indicator Code'}, inplace=True)

    # Melting the dataframe to make it long-form for the years
    df_long = pd.melt(df, id_vars=['Country', 'Country Code', 'Indicator Name', 'Indicator Code'],
                      var_name='Year', value_name='Infant Mortality Rate')
    df_long['Year'] = pd.to_numeric(df_long['Year'], errors='coerce')
    df_long = df_long.dropna(subset=['Year'])  # Dropping rows where 'Year' is NaN
    return df_long

def visualize_data(df, countries):
    # Filter data for specific countries
    df_filtered = df[df['Country'].isin(countries)]
    # Create a line chart
    fig = px.line(df_filtered, x='Year', y='Infant Mortality Rate', color='Country', 
                  title='Infant Mortality Rate Over Time')
    fig.show()

def main():
    filepath = 'Birthrate.csv'  # Full path to your CSV file
    df = load_and_clean_data(filepath)
    countries = ['United Arab Emirates', 'Australia', 'Austria']  # Example countries
    visualize_data(df, countries)

if __name__ == "__main__":
    main()
