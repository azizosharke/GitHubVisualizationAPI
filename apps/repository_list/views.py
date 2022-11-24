from flask import Blueprint, render_template, request, abort
from github import Github
import random

repository_list_bp = Blueprint("repository_list", __name__, url_prefix="/repository_list")


class UserInfo:
    def __init__(self, username, oauthToken):
        self.username = username
        self.oauthToken = oauthToken


# def getUserRepos(user):
#     repoCount = 0
#     repoNames = []

#     for repo in user.get_repos():
#         repoCount += 1
#         repoNames.append(repo.name)

#     ## returns array with repo names
#     return repoNames

@repository_list_bp.errorhandler(400)
def page_not_found(error):
    error = "error: enter a valid username"
    return render_template('login.html', error=error)

def getCommitsInRepo(user):
    repoNames = []
    countOfCommitsInRepo = []
    currentCountOfCommits = 0
    countOfRepos = 0

    for repo in user.get_repos():
        repoNames.append(repo.name)
        countOfRepos += 1
        currentCountOfCommits = 0
        for commit in repo.get_commits():
            currentCountOfCommits += 1
        countOfCommitsInRepo.append(currentCountOfCommits)

    formattedRepoArray = []
    for x in range(countOfRepos):
        tupleX = (repoNames[x], countOfCommitsInRepo[x])
        formattedRepoArray.append(tupleX)
    return formattedRepoArray, repoNames

##### Get breakdown of repos by language
def getLanguageBreakdown(user):
    language_count = ([], [])
    for repo in user.get_repos():
        print(repo)
        languages = repo.get_languages()
        for language in languages.keys():
            if language not in language_count[0]:
                language_count[0].append(language)
                language_count[1].append(1)
            else:
                language_count[1][language_count[0].index(language)] += 1

    return language_count
##### Method end

@repository_list_bp.route("/")
def showList():
    
    user_info = UserInfo(
        request.args.get("username"),
        request.args.get("oauthToken")
    )
    
    
    g = Github('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')
    try:
        user = g.get_user(user_info.username)
    except Exception:
        abort(400)
        
    user.login
    
    data2, repoNames = getCommitsInRepo(user)
    
    
    
    
    labels2 = [row[0] for row in data2]
    values2 = [row[1] for row in data2]
    
    labels3,values3 = getLanguageBreakdown(user)
    
    colorPalette = []
    
    for _ in range(len(labels3)):
        rgb = 'rgb(' + str(round(random.random() *255)) + ',' + str(round(random.random() *255)) + ',' + str(round(random.random() *255)) + ')'
        colorPalette.append(rgb)
    
    
    # repoNames = getUserRepos(user)
    
    return render_template("repository_list/repository.html", data = repoNames, username = user_info.username, labels2 = labels2, values2 = values2, labels3 = labels3, values3 = values3, colorList = colorPalette)