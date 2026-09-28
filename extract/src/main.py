import extractor.extractor as ex

# REPO_USER_NAME = 'symfony'
REPO_USER_NAME = 'google'
# repos = ex.fetch_repo(REPO_USER_NAME)
# with open('data/extract_tmp/fichier.txt', 'w',encoding='utf-8') as f:
#     for item in repos:
#         f.write(f'{item}\n')


issues = ex.fetch_issues(REPO_USER_NAME,'access-bridge-explorer')
print(issues)
with open('data/extract_tmp/issues.txt', 'w',encoding='utf-8') as f:
    for item in issues:
        f.write(f'{item}\n')