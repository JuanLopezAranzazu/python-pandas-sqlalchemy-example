import os
import pandas as pd
from sqlalchemy.sql import func
import matplotlib.pyplot as plt
from models.profession import Profession
from models.customer import Customer

# directorio
graphs_dir = "graphs"

# grafica de promedio de ingresos anuales por profesión
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


# grafica de cantidad de clientes por profesión
def plot_customers_by_profession(db):
  # consultar cantidad de clientes agrupados por profesión
  results = (
    db.query(Profession.name, func.count(Customer.id))
    .join(Customer, Profession.id == Customer.profession_id)
    .group_by(Profession.name)
    .all()
  )

  # convertir los datos a DataFrame de Pandas
  df = pd.DataFrame(results, columns=["Profession", "Customer Count"])

  # ordenar los datos por cantidad de clientes
  df = df.sort_values(by="Customer Count", ascending=False)

  # crear el gráfico de barras
  plt.figure(figsize=(11, 6))
  plt.barh(df["Profession"], df["Customer Count"], color="lightgreen")
  plt.xlabel("Cantidad de Clientes")
  plt.ylabel("Profesión")
  plt.title("Cantidad de Clientes por Profesión")
  plt.gca().invert_yaxis()
  
  # guardar el gráfico en un archivo
  plt.savefig(f"{graphs_dir}/customers_by_profession.png")
  plt.close()


# grafica de promedio de experiencia laboral por profesión
def plot_experience_by_profession(db):
  # consultar experiencia laboral promedio agrupada por profesión
  results = (
    db.query(Profession.name, func.avg(Customer.work_experience))
    .join(Customer, Profession.id == Customer.profession_id)
    .group_by(Profession.name)
    .all()
  )

  # convertir los datos a DataFrame de Pandas
  df = pd.DataFrame(results, columns=["Profession", "Avg Experience"])

  # ordenar los datos por experiencia laboral
  df = df.sort_values(by="Avg Experience", ascending=False)

  # crear el gráfico de barras
  plt.figure(figsize=(11, 6))
  plt.barh(df["Profession"], df["Avg Experience"], color="salmon")
  plt.xlabel("Experiencia Laboral Promedio (años)")
  plt.ylabel("Profesión")
  plt.title("Experiencia Laboral Promedio por Profesión")
  plt.gca().invert_yaxis()
  
  # guardar el gráfico en un archivo
  plt.savefig(f"{graphs_dir}/experience_by_profession.png")
  plt.close()


# crear gráficos
def generate_graphs(db):
  # crear directorio si no existe
  if not os.path.exists(graphs_dir):
    os.makedirs(graphs_dir)

  # crear gráficas
  plot_income_by_profession(db)
  plot_customers_by_profession(db)
  plot_experience_by_profession(db)

  print("Gráficas generadas en la carpeta 'graphs'")
