import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
import urllib.request

print("""
Exposant : Abdoulaye AW
Classe : E3 CCSN

DataOps avec Python données du Titanic
""")
print("\n")
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
data = urllib.request.urlopen(url)

print(" 1 - Pipeline Dataops")
print("\n")
# Charge les données du Titanic à partir de l'URL spécifiée dans un DataFrame.
def load_titanic_data(url):
    try:
        titanic_data = pd.read_csv(url)
        return titanic_data
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
        return None


# Récupération des données en utilisant la méthode optimisée
titanic_data = load_titanic_data(url)


# Convertit les données en JSON
def transform_data_to_JSON(titanic_data):
    # Sélectionner les colonnes pertinentes
    selected_columns = ["Sex", "Pclass", "Age", "Survived", "Fare", "Embarked"]
    passengers = titanic_data[selected_columns]

    # Renommer les colonnes pour correspondre au modèle JSON
    selected_columns = ["sex", "class", "age", "survived", "price", "embarked"]
    passengers.columns = selected_columns
    # Convertir le DataFrame en format JSON
    passenger_json = passengers.to_json(orient="records", lines=True)
    return passenger_json


# Formate les enregistrements JSON
def format_json_records(json_data):
    formatted_json_data = json_data.replace('},{', '},\n{')
    formatted_json_data = f"[{formatted_json_data}]"
    return formatted_json_data


# Transformer les données en JSON
json_data = transform_data_to_JSON(titanic_data)

# Formater les enregistrements JSON
formatted_json_data = format_json_records(json_data)

# Enregistrement des données
def save_to_json_file(json_data, file_path, indent=2):
    with open(file_path, "w") as json_file:
        json_file.write(json_data)


if titanic_data is not None:
    # Transformer les données en JSON
    json_data = transform_data_to_JSON(titanic_data)

    # Formater les enregistrements JSON
    formatted_json_data = format_json_records(json_data)

    # Personnaliser le nom et le chemin du fichier JSON
    json_file_path = "passenger.json"

    # Enregistrer le JSON dans un fichier
    save_to_json_file(formatted_json_data, json_file_path, indent=2)

    print(f"Modèle JSON enregistré avec succès dans le fichier {json_file_path}")
else:
    print("Échec du chargement des données. Veuillez vérifier votre connexion Internet ou l'URL du fichier CSV.")

print("2 - Traitement des donnees ")
print("\n------------------------------------------------------------------------")
# Fonction pour compter le nombre de femmes de moins de 18 ans qui ont survécu
def female_survived(titanic_data):
    # Filtrer les femmes de moins de 18 ans
    femmes_moins_18_ans = titanic_data[(titanic_data["Sex"] == "female") & (titanic_data["Age"] < 18)]

    # Compter le nombre de femmes de moins de 18 ans qui ont survécu
    nombre_femmes_moins_18_ans_survivantes = femmes_moins_18_ans["Survived"].sum()

    print(f"Nombre de femmes de moins de 18 ans qui ont survécu : {nombre_femmes_moins_18_ans_survivantes}")


# Appeler la fonction female_survived avec les données du fichier CSV
if titanic_data is not None:
    female_survived(titanic_data)
else:
    print("Échec du chargement des données depuis le fichier CSV.")

#Fonction pour calculer la répartition des morts et des survivants en fonction du port de départ
def calculate_survival_by_embarked(titanic_data):
    survival_by_embarked = titanic_data.groupby('Embarked')['Survived'].value_counts().unstack().fillna(0)
    return survival_by_embarked

# Afficher la répartition des morts et des survivants en fonction du port de départ
def display_survival_by_embarked(survival_by_embarked):
    print("Répartition des morts et des survivants en fonction du port de départ :")
    print(survival_by_embarked)


# Fonction pour réer un histogramme pour la répartition par sexe et par âge

def plot_age_distribution(titanic_data):
    plt.figure(figsize=(10, 6))
    titanic_data[titanic_data['Sex'] == 'male']['Age'].plot.hist(alpha=0.5, color='blue', bins=30, label='Hommes')
    titanic_data[titanic_data['Sex'] == 'female']['Age'].plot.hist(alpha=0.5, color='pink', bins=30, label='Femmes')
    plt.xlabel('Âge')
    plt.ylabel('Nombre de passagers')
    plt.legend()
    plt.title('Répartition par sexe et par âge des passagers du navire')
    plt.show()



# Calculer la répartition des morts et des survivants en fonction du port de départ
survival_by_embarked = calculate_survival_by_embarked(titanic_data)
print("\n------------------------------------------------------------------------")

# Afficher la répartition des morts et des survivants en fonction du port de départ
display_survival_by_embarked(survival_by_embarked)
print("\n-------------------------------------------------------------------------")

# Créer un histogramme pour la répartition par sexe et par âge des passagers du navire
plot_age_distribution(titanic_data)

print("FIN !")