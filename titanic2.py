import numpy as np
import pandas as pd
import json
import urllib.request

# Exposant : Abdoulaye AW Classe : E3 CCSN DataOps avec Python données du Titanic
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
data = urllib.request.urlopen(url) 

print("1 - Pipeline Dataops")

# Request data
def load_titanic_data(url):
    """
    Charge les données du Titanic à partir de l'URL spécifiée dans un DataFrame.
    """
    try:
        titanic_data = pd.read_csv(url)
        return titanic_data
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
        return None

# Récupération des données en utilisant la méthode optimisée
titanic_data = load_titanic_data(url)

# Convertir les données en JSON et enregistrer dans un fichier
def save_data_to_json(titanic_data, file_path):
    # Sélectionner les colonnes pertinentes
    selected_columns = ["Sex", "Pclass", "Age", "Survived", "Fare", "Embarked"]
    passengers = titanic_data[selected_columns]

    # Renommer les colonnes pour correspondre au modèle JSON
    selected_columns = ["sex", "class", "age", "survived", "price", "embarked"]
    passengers.columns = selected_columns

    # Convertir le DataFrame en format JSON
    passenger_json = passengers.to_json(orient="records", lines=True)

    # Ajouter les crochets `[` et `]` autour des données JSON
    passenger_json = "[" + passenger_json + "]"

    # Enregistrement des données dans un fichier JSON
    with open(file_path, "w") as json_file:
        json_file.write(passenger_json)

    print(f"Modèle JSON enregistré avec succès dans le fichier {file_path}")
# Chemin du fichier JSON à créer
json_file_path = "passenger.json"

# Convertir les données en JSON et enregistrer dans un fichier
def save_data_to_json(titanic_data, file_path):
    # Sélectionner les colonnes pertinentes
    selected_columns = ["Sex", "Pclass", "Age", "Survived", "Fare", "Embarked"]
    passengers = titanic_data[selecte
                              d_columns]

    # Renommer les colonnes pour correspondre au modèle JSON
    selected_columns = ["sex", "class", "age", "survived", "price", "embarked"]
    passengers.columns = selected_columns

    # Convertir le DataFrame en format JSON
    passenger_json = passengers.to_json(orient="records", lines=True)

    # Enregistrement des données dans un fichier JSON
    with open(file_path, "w") as json_file:
        json_file.write(passenger_json)

    print(f"Modèle JSON enregistré avec succès dans le fichier {file_path}")

# Chemin du fichier JSON à créer
json_file_path = "passenger.json"

# Enregistrez les données dans un fichier JSON
if titanic_data is not None:
    save_data_to_json(titanic_data, json_file_path)
else:
    print("Échec du chargement des données. Veuillez vérifier votre connexion Internet ou l'URL du fichier CSV.")

# Charger les données à partir d'un fichier JSON
def load_data_from_json(file_path):
    try:
        with open(file_path, 'r') as json_file:
            passenger_data = json.load(json_file)
        return pd.DataFrame(passenger_data)
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
        return None

print("2 - Traitement des donnees ")

# Charger les données à partir du fichier JSON
titanic_data_json = load_data_from_json("passenger.json")
# Fonction pour compter le nombre de femmes de moins de 18 ans qui ont survécu
def female_survived(titanic_data):
    # Filtrer les femmes de moins de 18 ans
    femmes_moins_18_ans = titanic_data[(titanic_data["sex"] == "female") & (titanic_data["age"] < 18)]

    # Compter le nombre de femmes de moins de 18 ans qui ont survécu
    nombre_femmes_moins_18_ans_survivantes = femmes_moins_18_ans["survived"].sum()

    print(f"Nombre de femmes de moins de 18 ans qui ont survécu : {nombre_femmes_moins_18_ans_survivantes}")


# Charger les données à partir du fichier JSON
titanic_data_json = load_data_from_json("passenger.json")

# Appeler la fonction female_survived avec les données chargées du fichier JSON
if titanic_data_json is not None:
    female_survived(titanic_data_json)
else:
    print("Échec du chargement des données depuis le fichier JSON.")

# Répartition par classe des femmes de moins de 18 ans qui ont survécu
if titanic_data_json is not None:
    femmes_moins_18_ans_survivantes = titanic_data_json[(titanic_data_json["sex"] == "female") & (titanic_data_json["age"] < 18) & (titanic_data_json["survived"] == 1)]
    repartition_par_classe = femmes_moins_18_ans_survivantes["class"].value_counts()
    print("Répartition par classe des femmes de moins de 18 ans qui ont survécu :")
    print(repartition_par_classe)
else:
    print("Échec du chargement des données depuis le fichier JSON.")

# Répartition des morts et des survivants en fonction du port de départ
if titanic_data_json is not None:
    repartition_par_port = titanic_data_json.groupby("embarked")["survived"].value_counts()
    print("Répartition des morts et des survivants en fonction du port de départ :")
    print(repartition_par_port)
else:
    print("Échec du chargement des données depuis le fichier JSON.")

# Répartition par sexe et par âge des passagers du navire
if titanic_data_json is not None:
    repartition_par_sexe_et_age = titanic_data_json.groupby(["sex", pd.cut(titanic_data_json["age"], np.arange(0, 100, 10))]).size().unstack(fill_value=0)
    print("Répartition par sexe et par âge des passagers du navire :")
    print(repartition_par_sexe_et_age)
else:
    print("Échec du chargement des données depuis le fichier JSON.")
