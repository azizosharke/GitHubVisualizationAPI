from flask import Blueprint, render_template, request, abort
from github import Github

repository_list_bp = Blueprint("repository_list", __name__, url_prefix="/repository_list")


class UserInfo:
    def __init__(self, username, oauthToken):
        self.username = username
        self.oauthToken = oauthToken;


def getUserRepos(username, token):
    # change this to user's token
    auth_token = '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'

    g = Github(auth_token)

    try:
        user = g.get_user(username)
    except Exception:
        abort(400)

    user.login

    repoCount = 0
    repoNames = []

    for repo in user.get_repos():
        repoCount += 1
        repoNames.append(repo.name)

    ## returns array with repo names
    return repoNames

@repository_list_bp.errorhandler(400)
def page_not_found(error):
    error = "error: enter a valid username"
    return render_template('login.html', error=error)

def getCommitsInRepo(userInput):
    auth_token = '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'
    username = userInput

    g = Github(auth_token)

    try:
        user = g.get_user(username)
    except Exception:
        abort(400)

    user.login

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
    return formattedRepoArray

@repository_list_bp.route("/")
def showList():
    
    user_info = UserInfo(
        request.args.get("username"),
        request.args.get("oauthToken")
    )
    
    data2 = getCommitsInRepo(user_info.username)
    
    data3 = [
        ("15-01-2020", 18),
        ("16-01-2020", 15),
        ("17-01-2020", 6),
        ("18-01-2020", 14),
        ("19-01-2020", 9),
        ("20-01-2020", 12),
        ("21-01-2020", 25),
    ]
    
    labels2 = [row[0] for row in data2]
    values2 = [row[1] for row in data2]
    
    labels3 = [row[0] for row in data3]
    values3 = [row[1] for row in data3]
    
    repoNames = getUserRepos(user_info.username, user_info.oauthToken)
    
    return render_template("repository_list/repository.html", data = repoNames, username = user_info.username, labels2 = labels2, values2 = values2, labels3 = labels3, values3 = values3)