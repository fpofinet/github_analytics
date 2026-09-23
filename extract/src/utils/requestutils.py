
def extract_query_parm (url):
    """
        Cette fonction permet d'extraire les queries param d'une url.
        Elle prend en prend en parametre l'url et renvoi un dictionnaire 
        contenant les queries param
    """
    query_param_dict ={}
    #on recupere la chaine contenant les queries parameters
    query_param_string = url[url.find('?')+1:]
    """
        on utilise la comprehension de liste pour decouper la chaine query_param_string
        les symboles '&' afin de recuperer chaque query param que l'on separe avec les 
        symbole '=' pour obtenir des listes ou le premier element est la clef et le second la valeur
        on utilise ensuite de la comprehension de dictionnaire pour constituer un dict avec
        le query param comme clef et sa valeur  comme valeur de la clef du dict 
    """
    query_param_dict={
        item[0]:item[1] for item in [
            item.split('=') for item in query_param_string.split('&')
        ]
    }
    #print(query_param_string)
    return query_param_dict


def extract_last_page_url(header):
    """
        Cette fonction permetde verifier et d'extraire l'url de la derniere page.
        Elle prend en parametre la valeur du header link et renvoi
        1- une chaine contenant l'url de la derniere page si elle existe
        2- None si aucune url contenant a la derniere page n'est trouver dans 
           le headers link
    """
    #on separe la chaine en list avec les symboles ','
    header_list = header.split(',')
    # on utilise la comprehension de list pour recuperer l'element contenant 
    # la valeur 'rel="last"' qui represente l'url de la derniere page
    last_page_item =[item for item in header_list if 'rel="last"' in item]
    #on verifie last_page_item contient un element, si oui on continue si non on renvoi none
    if(len(last_page_item ) > 0):
        last_page_url = last_page_item[0]
        #on nettoie l'url en eliminant les chevrons de debut et de fin
        cleaned_last_url = last_page_url[last_page_url.find('<')+1:last_page_url.find('>')]
        return cleaned_last_url
    return None