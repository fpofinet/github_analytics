"""
    ce module permet l'extraction des repositories et issues depuis les APIs de  GitHub
"""
import requests
import logging
import utils.requestutils as reu
import utils.extractutils as exu

def fetch_repo(user_name):
    """
        Cette fonction nous permet de toutes les repositories d'un compte
        Elle prend en paramètre le username et renvoie une liste contenant 
        les dépôts appartenant à ce username
    """
    repos = list()
    try :
        url = f'https://api.github.com/users/{user_name}/repos?per_page=100'
        #on effectue une premiere requete pour recuperer les infos sur les repos du user
        response = requests.get(url=url)
        response.raise_for_status()
        page_count=1
        if('Link' in response.headers):
            #on extrait le nombre total de page 
            last_page_url= reu.extract_last_page_url(response.headers["Link"])
            params= reu.extract_query_parm(last_page_url)
            page_count = params['page']
            #On recuperer tout les repositories page par pages
            for page in range(1,int(page_count)+1):
                url = url+f'&page={page}'
                response = requests.get(url=url)
                response.raise_for_status()
                repos.extend(response.json()) 
                logging.info(f"Recuperation des repositories de : {user_name} ==>  page : {page}")
        else :
            repos.extend(response.json())
            logging.info(f"Recuperation des repositories de : {user_name} ==>  page All")
    except requests.exceptions.RequestException as e:
        logging.error(f"Échec de récupération des repositories de  {user_name} : {e}")
        return None

    return repos

def fetch_issues(owner,repo):
    """
        Cette fonction nous permet de toutes les issues d'un repository
        Elle prend en paramètre le username du owner et le nom du repository 
        et renvoie une liste contenant les issues de ce repository
    """
   
    issues = list()
    try :
        url = f'https://api.github.com/repos/{owner}/{repo}/issues?per_page=100'
        response = requests.get(url=url)
        response.raise_for_status()
        page_count=1
        #print(response.headers)
        if('Link' in response.headers):
            #on extrait le nombre total de page 
            last_page_url= reu.extract_last_page_url(response.headers["Link"])
            params= reu.extract_query_parm(last_page_url)
            page_count = params['page']
            for page in range(1,int(page_count)+1):
                url = url+f'&page={page}'
                resp = requests.get(url=url)
                resp.raise_for_status()
                issues.extend(resp.json())
                logging.info(f"Recuperation des issues de {owner} sur le repos {repo} ==>  page : {page}")
        else :
            issues.extend(response.json())
            logging.info(f"Recuperation des issues de {owner} sur le repos {repo} ==>  page : ALL")
    except requests.exceptions.RequestException as e:
        logging.error(f"Echec de recuperation des issues de {owner} sur le repos {repo} : {e}")
        return None
    
    return issues

def fetch_all_issues(repos_file_path,owner_name):
    """
        Cette fonction nous permet de récupérer toutes les issues de tous les dépôts
        Elle prend en paramètre le chemin vers le fichier de sauvegarde des donnees brutes des 
        repositories et renvoie un dictionnaire contenant toutes les issues de tous les
        repositionne : les clefs du dictionnaire sont les noms de dépositoire et les valeurs
        les issues
    """
    issues_dict = dict()
    repo_names = exu.get_repo_names(repos_file_path)
    try:
        for repo_name in repo_names:
            logging.info(f"Recuperation des issues du  repo {repo_name}")
            issues_dict[repo_name] = fetch_issues(owner_name,repo_name)
    except Exception as e:
        logging.error(f"Echec de recuperation des issues : {e}")

    return issues_dict
