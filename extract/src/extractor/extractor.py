"""
    ce module permet l'extraction des donnees issues des repos github
"""
import requests
import logging
import utils.requestutils as ru

def fetch_repo(user_name):
    """
        Cette fonction nous permet de tout les repositories d'un user
        donnees en params les taux de changes
    """
   
    rates = list()
    try :
        url = f'https://api.github.com/users/{user_name}/repos?per_page=100'
        #on effectue une premiere requete pour recuperer les infos
        response = requests.get(url=url)
        response.raise_for_status()
        page_count=1
        if('Link' in response.headers):
            #on extrait le nombre total de page 
            last_page_url= ru.extract_last_page_url(response.headers["Link"])
            params= ru.extract_query_parm(last_page_url)
            page_count = params['page']
            #print(page_count)
            for page in range(1,int(page_count)+1):
                url = url+f'&page={page}'
                response = requests.get(url=url)
                response.raise_for_status()
                rates.append(response.json()) 
                print(f"Recuperation des repositories de : {user_name} ==>  page : {page}")
                logging.info(f"Recuperation des repositories de : {user_name} ==>  page : {page}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Echec de recuperation des repositories de  {user_name} : {e}")
        return None

    # print(rates)
    return rates

def fetch_issues(owner,repo):
    """
        Cette fonction nous permet de tout les ussues d'un repositories
        d'un user donnees en params les taux de changes
    """
   
    rates = dict()
    try :
        url = f'https://api.github.com/repos/{owner}/{repo}/issues'
        response = requests.get(url=url)
        response.raise_for_status()
        logging.info(f"Recuperation des issues de {owner} sur le repos {repo}")
        #print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Echec de recuperation des issues de {owner} sur le repos {repo} : {e}")
        return None
    
    return rates



################### UTILS