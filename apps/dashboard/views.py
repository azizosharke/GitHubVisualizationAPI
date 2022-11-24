from array import *
from flask import Blueprint, render_template, request
from github import Github
import datetime as DT
from datetime import timedelta as TD

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

todayDate = DT.date.today()
todayDT = DT.datetime.now()


def last_seven_days_pos(x):
    diff = (todayDate - x).days

    return (6-diff)
        
##### Method end

commitsDay0 = 0
day0 = (todayDT - TD(days=6)).strftime("%d-%m-%Y")
commitsDay1 = 0
day1 = (todayDT - TD(days=5)).strftime("%d-%m-%Y")
commitsDay2 = 0
day2 = (todayDT - TD(days=4)).strftime("%d-%m-%Y")
commitsDay3 = 0
day3 = (todayDT - TD(days=3)).strftime("%d-%m-%Y")
commitsDay4 = 0
day4 = (todayDT - TD(days=2)).strftime("%d-%m-%Y")
commitsDay5 = 0
day5 = (todayDT - TD(days=1)).strftime("%d-%m-%Y")
commitsDay6 = 0
day6 = todayDT.strftime("%d-%m-%Y")

def formatArrayForReturn(x0, x1, x2, x3, x4, x5, x6):
    tuple0 = (day0, x0)
    tuple1 = (day1, x1)
    tuple2 = (day2, x2)
    tuple3 = (day3, x3)
    tuple4 = (day4, x4)
    tuple5 = (day5, x5)
    tuple6 = (day6, x6)
    formattedTupleArray = [tuple0, tuple1, tuple2, tuple3, tuple4, tuple5, tuple6]

    return formattedTupleArray


def getCommitsFromLast7Days(user, repoInput):

    global commitsDay0, commitsDay1, commitsDay2, commitsDay3, commitsDay4, commitsDay5, commitsDay6

    ## go through repos
    for repo in user.get_repos():

        ## if repo matches selected repository
        if repo.name == repoInput:

            # we access the commit
            for commit in repo.get_commits():

                # if a commit is made by the logged-in user
                if commit.author == user: 

                    #we access the date the commit was made
                    commitDate = commit.commit.author.date

                    #turn it into a datetime object
                    date1 = DT.date(commitDate.year, commitDate.month, commitDate.day)

                    # check whether it was made within the last seven days
                    # last seven_days_pos returns 0 if the change was made 6 days ago, 1 if it was made 5 days ago, etc.
                    # last_seven_days_pos max return value is 6 <-- last index in the array to return
                    day_in_array = last_seven_days_pos(date1)

                    # check if commit was made within the last seven days
                    if (day_in_array >=0):

                        ## adding commits to counts per day
                        match day_in_array:
                            case 0:
                                commitsDay0 += 1
                            case 1:
                                commitsDay1 += 1
                            case 2:
                                commitsDay2 += 1
                            case 3:
                                commitsDay3 += 1
                            case 4:
                                commitsDay4 += 1
                            case 5:
                                commitsDay5 += 1
                            case 6:
                                commitsDay6 += 1
                            case _:
                                continue
            break

    ## forming the array to return
    commitsPerDay = formatArrayForReturn(commitsDay0, commitsDay1, commitsDay2, commitsDay3, commitsDay4, commitsDay5, commitsDay6)

    return commitsPerDay


def getRepoLanguages(repoName,user):

    try:
        repo = user.get_repo(repoName)
    except:
        print("Error: Repo not found")
        return
    line_count = ([], [])
    langsDict = repo.get_languages()
    for language in langsDict.keys():
        line_count[0].append(language)
        line_count[1].append(langsDict[language])
    return line_count
#### Method end

@dashboard_bp.route("/")
def graph():
    nameWithRepo = request.args.get("value")
    spaceIndex = nameWithRepo.find(" ")
    
    username = nameWithRepo[0:spaceIndex]
    repoName = nameWithRepo[spaceIndex+1:]
    
    g = Github('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')
    user = g.get_user(username)
        
    user.login
    
    data1 = getCommitsFromLast7Days(user, repoName)

    labels1 = [row[0] for row in data1]
    values1 = [row[1] for row in data1]
 

    # DOESNT WORK 
    labels2,values2 = getRepoLanguages(repoName,user)



    
    
    return render_template("dashboard/graph.html", labels1 = labels1, values1 = values1,labels2 = labels2, values2 = values2, username = username, repoName = repoName)
