import pandas as pd
from models.profession import Profession
from models.customer import Customer

# ruta del archivo csv
csv_file = "./data/customers.csv"

def load_customer_data(db):
  # leer el archivo csv
  dataFrame = pd.read_csv(csv_file)

  # insertar los datos en la base de datos

  try:
    with db.begin():
      # verificar si la tabla de profesiones está vacía
      if db.query(Profession).count() == 0:
        # insertar las profesiones
        professions = [{"name": profession} for profession in dataFrame["Profession"].dropna().unique()]
        db.bulk_insert_mappings(Profession, professions)

      # verificar si la tabla de clientes está vacía
      if db.query(Customer).count() == 0:
        # insertar los clientes
        customers = []
        for _, row in dataFrame.iterrows():
          profession_name = row["Profession"]
                    
          if pd.isna(profession_name):
            profession_id = None
          else:
            profession_id = db.query(Profession.id).filter(Profession.name == profession_name).scalar()

          customer = {
            "gender": row["Gender"],
            "age": row["Age"],
            "annual_income": row["Annual Income ($)"],
            "spending_score": row["Spending Score (1-100)"],
            "work_experience": row["Work Experience"],
            "family_size": row["Family Size"],
            "profession_id": profession_id
          }
          customers.append(customer)

        db.bulk_insert_mappings(Customer, customers)

    db.commit() # guardar los cambios

  except Exception as e:
    db.rollback()  # si hay un error
    print(f"Error: {e}")

  finally:
    db.close()