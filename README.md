# 📊 Análisis de Ventas: Pipeline ETL y Dashboard

## 📝 Descripción del Proyecto
Este proyecto demuestra un flujo de trabajo completo de análisis de datos, comenzando desde la extracción y limpieza de datos crudos utilizando **Python**, su almacenamiento estructurado en una base de datos **SQLite**, y la visualización de métricas clave a través de un dashboard interactivo en **Power BI**.

> **Nota:** Los datos utilizados en este proyecto fueron generados de forma aleatoria con fines de demostración técnica y no representan información real o confidencial.

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python (Pandas, NumPy)
* **Base de Datos:** SQLite (SQLAlchemy)
* **Visualización:** Power BI
* **Entorno:** Jupyter Notebook, VS Code

## ⚙️ Arquitectura del Pipeline (ETL)
1. **Extracción (Extract):** Lectura de registros transaccionales desde un archivo Excel (`Ventas_Crudas.xlsx`).
2. **Transformación (Transform):** * Remoción de valores nulos y registros duplicados.
   * Estandarización de columnas de texto (formato *snake_case*) y normalización de fechas/horas.
   * Ingeniería de características (Feature Engineering): Cálculo de la métrica de *Ganancia Neta* en el backend.
3. **Carga (Load):** Inserción de los datos limpios en una tabla relacional de SQLite (`ventas.db`) para su posterior conexión con Power BI.

## 📈 Dashboard y Resultados Visuales
El dashboard diseñado permite explorar las tendencias de ventas, analizar las ganancias por categoría de producto y evaluar el rendimiento general del negocio.

![Vista previa del Dashboard](dashboard/dashboard_preview.pdf)

## 📂 Estructura del Repositorio
- `/notebooks`: Contiene el archivo `limpieza_y_analisis.ipynb` con la documentación paso a paso del análisis exploratorio (EDA) y la limpieza.
- `/src`: Scripts de automatización en Python (`procesar_ventas.py` y `Discrepancies.py`).
- `/data`: Archivos de datos originales y procesados.
- `/database`: Archivo local de SQLite (`ventas.db`).
- `Dashboard_Ventas.pbix`: Archivo fuente de Power BI.

## 🚀 Cómo ejecutar el código localmente
1. Clona este repositorio: `git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git`
2. Instala las dependencias necesarias: `pip install pandas numpy sqlalchemy openpyxl`
3. Ejecuta el script principal de ETL: `python src/procesar_ventas.py`