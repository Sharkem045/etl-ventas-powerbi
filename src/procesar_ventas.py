import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def load_data(file_path = 'data/raw/Ventas_Crudas.xlsx' ):
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None
    
def clean_data(data):
    data = data.dropna() 
    data = data.drop_duplicates()
    data.columns = data.columns.str.lower().str.strip().str.replace(' ', '_')
    data['fecha'] = pd.to_datetime(data['fecha'], errors='coerce').dt.date  # Clean fecha column
    data['hora'] = pd.to_datetime(data['hora'], format='%H:%M', errors='coerce').dt.strftime('%H:%M') # Convert hora to time format
    data.rename(columns={'categoría': 'categoria'}, inplace=True)
    data['ganancia_neta'] = data['precio_venta'] - data['costo_insumos']  # Calculate net profit

    # Clean specific columns
    columns = ['categoria', 'producto']
    for col in columns:
        data[col] = data[col].str.lower().str.strip().str.replace(' ', '_')
    
    return data

def save_data_to_database(data, db_url, table_name, file_path='data/processed/Ventas_Limpias.xlsx'):
    try:
        engine = create_engine(db_url)
        data.to_sql(table_name, con=engine, if_exists='replace', index=False)
        data.to_excel(file_path, index=False)
        print(f"Data saved to database table '{table_name}' successfully.")
        print(f"Data saved in a new xlsx '{file_path}' successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

def main():
    # Load the data from the Excel file   
    data = load_data()
    
    if data is not None:
        print("Data loaded successfully:")
        # Clean the data
        cleaned_data = clean_data(data)
        print("Data cleaned successfully:")
        print(cleaned_data.head())

        # Save the cleaned data to the database
        db_url = 'sqlite:///database/ventas.db'  
        table_name = 'historial_ventas'
        save_data_to_database(cleaned_data, db_url, table_name)

    else:
        print("Failed to load data.")


if __name__ == "__main__":
    main()