"""
    ce module permet de charger les données en bases de données
"""
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import LONGTEXT
import logging

# Création de la connexion a la base de donnees mysql
db_engine = create_engine('mysql+pymysql://root:@localhost/data_git_analytics')

def load_repositories(repo_file_path):
    """
        cette méthode permet de charger les repositories en bases de données
        Elle prend en paramètre le chemin du fichier CSV transformé
    """
    try:
        df = pd.read_csv(repo_file_path)
        df.to_sql('repositories', db_engine, if_exists='replace', index=False)
        logging.info(f"Chargement des repositories effectué avec succès")
    except Exception as e:
        logging.error(f"Erreur lors du chargement des repositories  en base de données : {e}")

def load_issues(issues_file_path):
    """
        cette méthode permet de charger les repositories en bases de données
        Elle prend en paramètre le chemin du fichier CSV transformé
    """
    try:
        df = pd.read_csv(issues_file_path)
        df.to_sql('issues', db_engine, if_exists='replace', index=False,dtype={"body": LONGTEXT()})
        logging.info(f"Chargement des issues effectué avec succès")
    except Exception as e:
            logging.error(f"Erreur lors du chargement des issues  en base de données : {e}")