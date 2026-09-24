import extractor.extractor as ex

# REPO_USER_NAME = 'symfony'
REPO_USER_NAME = 'google'
repos = ex.fetch_repo(REPO_USER_NAME)
with open('fichier.txt', 'w',encoding='utf-8') as f:
    for item in repos:
        f.write(f'{item}\n')