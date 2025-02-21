from db.database import engine, Base, SessionLocal
from utils.load_data import load_customer_data
from utils.create_graphs import plot_income_by_profession

# crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# crear una sesión de la base de datos
db = SessionLocal()

def main():
  # cargar los datos en la base de datos
  load_customer_data(db)

  # mostrar los gráficos
  plot_income_by_profession(db)

if __name__ == "__main__":
  main()
