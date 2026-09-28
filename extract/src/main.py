import extractor.extractor as ex

# REPO_USER_NAME = 'symfony'
REPO_USER_NAME = 'google'
REPO_TEMP_FILE_PATH = 'data/extract_tmp/all_repo_clean_28_09_2026.txt'
# repos = ex.fetch_repo(REPO_USER_NAME)
# with open('data/extract_tmp/fichier.txt', 'w',encoding='utf-8') as f:
#     for item in repos:
#         f.write(f'{item}\n')

print(f'################## Recuperation des names de repos ###################')
data = ex.fetch_all_issues(REPO_TEMP_FILE_PATH,REPO_USER_NAME)
# issues = ex.fetch_issues(REPO_USER_NAME,'access-bridge-explorer')
print(data)
# with open('data/extract_tmp/issues.txt', 'w',encoding='utf-8') as f:
#     for item in issues:
#         f.write(f'{item}\n')