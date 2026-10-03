"""
    Ce module permet de nettoyer et  formater les données brutes en données prêtes 
    à être inséré en base de données
"""
import ast
import logging
import pandas as pd
import json

def format_repos_data(raw_data_file_path,formatted_data_file_path):
    """
        Cette fonction permet de formater les repositories.
        Elle prend en compte le chemin du fichier de données brutes
        et le chemin du fichier csv de données transformé ou stocké les données
        transformé.
    """
    #liste des colonnes selectionner
    selected_columns =['id','node_id','name','full_name','private','owner','fork',
                      'description','html_url','language','visibility','default_branch',
                      'created_at','updated_at','pushed_at','watchers_count','forks_count']
    repos_datas= list()
    #recuperation des données depuis le fichier 
    try:
        with open(raw_data_file_path, "r",encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                repos_datas.append(ast.literal_eval(line))
        logging.error(f"Lecture du fichier {raw_data_file_path} terminée avec succès")
    except Exception as e:
        logging.error(f"Erreur lors de la lecture du fichier des repositories {raw_data_file_path} : {e}")
    try:
        #on creer un dataframe 
        df = pd.DataFrame(repos_datas)
        #on selectionne uniquement les colonnes importantes et on sauvegarde cela dans un fichier csv
        df = df[selected_columns]
        df.to_csv(formatted_data_file_path)
        logging.error(f"Repositories formatées chargées avec succès dans le fichier {formatted_data_file_path}")
    except Exception as e :
        logging.error(f"Erreur lors du chargement des repositories : {e}")
    
def format_issues_data(raw_data_file_path,formatted_data_file_path):
    """
        Cette fonction permet de formater les repositories.
        Elle prend en compte le chemin du fichier de données brutes
        et le chemin du fichier csv de données transformé ou stocké les données
        transformé.
    """
    issues_data = dict()
    try:
        with open(raw_data_file_path, 'r',encoding='utf-8') as f:
            issues_data = json.loads(f.read())
        logging.error(f"Lecture du fichier {raw_data_file_path} terminée avec succès")
    except Exception as e:
        logging.error(f"Erreur lors du chargement des repositories : {e}")
    
    #on applatit toutes les valeurs du dictionnaire dans une liste
    flatten_data = list()
    for values in issues_data.values():
        flatten_data.extend(values)
   
    try:
        #on convertit le tout en dataframe pour le manupuler plus facilement
        df = pd.DataFrame(flatten_data)
        #on selectionne les colonnes utiles
        selected_columns=['id','number','html_url','node_id','title','state','locked','comments','created_at',
                        'updated_at','closed_at','body','closed_by','author_association']
        #on selectionne uniquement les colonnes importantes et on sauvegarde cela dans un fichier csv
        df = df[selected_columns]
        df.to_csv(formatted_data_file_path)
        logging.error(f"Issues formatées chargées avec succès dans le fichier {formatted_data_file_path}")
    except Exception as e :
            logging.error(f"Erreur lors du chargement des issues : {e}")