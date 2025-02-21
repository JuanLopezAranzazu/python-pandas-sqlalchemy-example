import os
import pandas as pd
from sqlalchemy.sql import func
import matplotlib.pyplot as plt
from models.profession import Profession
from models.customer import Customer

# directorio
graphs_dir = "graphs"

def plot_income_by_profession(db):
  # consultar ingresos anuales agrupados por profesión
  results = (
    db.query(Profession.name, func.avg(Customer.annual_income))
    .join(Customer, Profession.id == Customer.profession_id)
    .group_by(Profession.name)
    .all()
  )

  # convertir los datos a DataFrame de Pandas
  df = pd.DataFrame(results, columns=["Profession", "Avg Annual Income"])

  # ordenar los datos por ingresos anuales
  df = df.sort_values(by="Avg Annual Income", ascending=False)

  # crear el gráfico de barras
  plt.figure(figsize=(11, 6))
  plt.barh(df["Profession"], df["Avg Annual Income"], color="skyblue")
  plt.xlabel("Ingreso Anual Promedio ($)")
  plt.ylabel("Profesión")
  plt.title("Ingreso Anual Promedio por Profesión")
  plt.gca().invert_yaxis()
  
  # crear el directorio si no existe
  os.makedirs(graphs_dir, exist_ok=True)
  # guardar el gráfico en un archivo
  plt.savefig(f"{graphs_dir}/income_by_profession.png")
  plt.close()
