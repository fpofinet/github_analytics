"""
    Ce module permet de formatter les payloads
"""
import ast
import logging
import pandas as pd
import json

def format_repos_data(raw_data_file_path,formatted_data_file_path):
    """cette fonction permet de formatter les repos"""
    #liste des colonnes selectionner
    selected_columns =['id','node_id','name','full_name','private','owner','fork',
                      'description','html_url','language','visibility','default_branch',
                      'created_at','updated_at','pushed_at','watchers_count','forks_count']
    repos_datas= list()
    #recuperation des donnees 
    try:
        with open(raw_data_file_path, "r",encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                repos_datas.append(ast.literal_eval(line))
    except Exception as e:
        logging.error(f"Erreur lors de la recuperation des repositories : {e}")
    try:
        #on creer un dataframe 
        df = pd.DataFrame(repos_datas)
        #on selectionne uniquement les colonnes importantes et on sauvegarde cela dans un fichier csv
        df = df[selected_columns]
        df.to_csv(formatted_data_file_path)
    except Exception as e :
        logging.error(f"Erreur lors de la recuperation des repositories : {e}")
    
def format_issues_data(raw_data_file_path,formatted_data_file_path):
    """Cette fonction permet de formmatter les issues"""
    issues_data = dict()
    with open(raw_data_file_path, 'r',encoding='utf-8') as f:
        issues_data = json.loads(f.read())

    #on applatit toutes les valeurs du dictionnaire dans une liste
    flatten_data = list()
    for values in issues_data.values():
        flatten_data.extend(values)

    #on convertit le tout en dataframe pour le manupuler plus facilement
    df = pd.DataFrame(flatten_data)

    #on selectionne les colonnes utiles
    selected_columns=['id','number','html_url','node_id','title','state','locked','comments','created_at',
                     'updated_at','closed_at','body','closed_by','author_association']
    #on selectionne uniquement les colonnes importantes et on sauvegarde cela dans un fichier csv
    df = df[selected_columns]
    df.to_csv(formatted_data_file_path)