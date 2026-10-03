import extractor.extractor as ex
import formatter.formatter as ft
import loader.loader as ld
import json
import logging

# Configuration des logs (écriture dans un fichier + affichage console)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler()
    ]
)


# REPO_USER_NAME = 'symfony'
#DECLARATION DES CONSTANTES
REPO_OWNER_NAME = 'google'
REPO_RAW_TEMP_FILE_PATH = 'data/extract_tmp/repos_raw_data.txt'
ISSUES_RAW_TEMP_FILE_PATH = 'data/extract_tmp/issues_raw_data.txt'
REPO_FORMATTED_FILE_PATH = 'data/format_tmp/repo_formatted.csv'
ISSUES_FORMATTED_FILE_PATH = 'data/format_tmp/issues_formatted.csv'


def run_pipeline():
    print(f'################## LANCEMENT DU PIPELINE ###################')

    print(f'################## LANCEMENT DE LA RECUPERATION DES REPOSITORIES ###################')
    repos = ex.fetch_repo(REPO_OWNER_NAME)

    print(f'################## SAUVEGARDE DES REPOSITORIES DANS UN FICHIER ###################')
    with open(REPO_RAW_TEMP_FILE_PATH, 'w',encoding='utf-8') as f:
        for item in repos:
            f.write(f'{item}\n')

    print(f'################## LANCEMENT DE LA RECUPERATION DES ISSUES DE CHAQUE REPOS ###################')
    issues_data = ex.fetch_all_issues(REPO_RAW_TEMP_FILE_PATH,REPO_OWNER_NAME)

    print(f'################## SAUVEGARDE DES ISSUES DANS UN FICHIER ###################')
    with open(ISSUES_RAW_TEMP_FILE_PATH, 'w',encoding='utf-8') as f:
        json.dump(issues_data, f, ensure_ascii=False, indent=4)

    print(f'################## FORMATTAGE DES DONNEES ###################')
    ft.format_repos_data(REPO_RAW_TEMP_FILE_PATH,REPO_FORMATTED_FILE_PATH)
    ft.format_issues_data(ISSUES_RAW_TEMP_FILE_PATH,ISSUES_FORMATTED_FILE_PATH)

    print(f'################## CHARGEMENT DES DONNEES DANS LA BASE DE DONNEES ###################')
    ld.load_repositories(REPO_FORMATTED_FILE_PATH)
    ld.load_issues(ISSUES_FORMATTED_FILE_PATH)
    print(f'################## FIN DU PIPELINE ###################')


if __name__ == "__main__":
    run_pipeline()