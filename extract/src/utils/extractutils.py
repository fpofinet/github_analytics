"""
    Ce module contient toute les fonctions utilitaire necessaire a l'extraction
"""
import ast
import logging

def get_repo_names(repos_data_file_path):
    """
        Cette fonction permet recuperer le name de tout les repositories
        Elle prend en parametre la liste contenant les dictionnaire des repositories
        et renvoie une liste contenant le name des repositories
    """
    repo_names = list()
    try:
        with open(repos_data_file_path, "r",encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                repo_names.append(ast.literal_eval(line)["name"])
    except Exception as e:
        logging.error(f"Erreur lors de la recuperation de non de repository : {e}")
        return None
    return repo_names

def extract_repository_name(repos):
    """
        Cette fonction permet de recuperer tout les noms des repositories.
        Elle prend en parametre la liste des repositories et renvoi une liste
        contenant les noms des repositories
    """