from db.database import engine, Base, SessionLocal
from utils.load_data import load_customer_data
from utils.create_graphs import generate_graphs

def main():
  # crear las tablas en la base de datos
  try:
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas correctamente")
  except Exception as e:
    print("Error al crear las tablas:", e)

  # crear una sesión de la base de datos
  db = SessionLocal()

  # cargar los datos en la base de datos
  load_customer_data(db)
  # crear gráficos
  generate_graphs(db)

if __name__ == "__main__":
  main()
