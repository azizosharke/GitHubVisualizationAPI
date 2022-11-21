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

@repository_list_bp.route("/")
def showList():
    
    user_info = UserInfo(
        request.args.get("username"),
        request.args.get("oauthToken")
    )
    
    repoNames = getUserRepos(user_info.username, user_info.oauthToken)
    
    return render_template("repository_list/repository.html", data = repoNames, username = user_info.username)