from sqlalchemy import create_engine, select, text
import pandas as pd
import numpy as np

def load_data(path):
    try:
        data = pd.read_excel(path)
        return data
    except Exception as e:
        print(f"Error loading data from {path}: {e}")
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

def load_data_from_database(db_url, table_name):
    try:
        engine = create_engine(db_url)
        with engine.connect() as connection:
            query = select('*').select_from(text(table_name))
            result = connection.execute(query)
            data = pd.DataFrame(result.fetchall(), columns=result.keys())
            return data
    except Exception as e:
        print(f"Error loading data from database: {e}")
        return None
    

def main():
    # Load the data from the Excel file
    file_path = 'Ventas_Crudas.xlsx' 
    data = load_data(file_path)
    
    if data is not None:
        print("Data loaded successfully:")
        # Clean the data
        cleaned_data = clean_data(data)
        print("Data cleaned successfully:")
        print(cleaned_data.head())


        # Load data from the database to verify
        db_url = 'sqlite:///ventas.db'  # Example database URL (SQLite)
        table_name = 'historial_ventas'

        loaded_data = load_data_from_database(db_url, table_name)
        if loaded_data is not None:
            print("Data loaded from database successfully:")
            print(loaded_data.head())
        else:
            print("Failed to load data from database.")

        for (idx_loaded, row_loaded), (_, row_cleaned) in zip(
            loaded_data.iterrows(), cleaned_data.iterrows()
        ):
            if row_loaded['precio_venta'] != row_cleaned['precio_venta']:
                print(
                    f"Discrepancy found in row {idx_loaded}: "
                    f"Database precio_venta = {row_loaded['precio_venta']}, "
                    f"Cleaned precio_venta = {row_cleaned['precio_venta']}"
                )
    else:
        print("Failed to load data.")

if __name__ == "__main__":
    main()