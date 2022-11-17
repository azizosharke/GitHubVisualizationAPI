from flask import Blueprint, render_template

repository_list_bp = Blueprint("repository_list", __name__, url_prefix="/repository_list")

@repository_list_bp.route("/")
def showList():
    data = [
        "repository1",
        "repository2",
        "repository3",
        "repository4",
        "repository5",
        "repository6",
        "repository7",
    ]
    
    return render_template("repository_list/repository.html", data = data)