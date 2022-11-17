# GitHubVisualizationAPI
Assignment 3 for CSU33012 SOFTWARE ENGINEERING - Main project

##　How to run on vscode

###　Always on the directry of the project folder

###　On Terminal　　
  conda create -n <env name you want to make> python=3.9
  conda activate <env name you jast made>

###　on vscode　　
  type python select interpreter in the command palette
  select interpreter with the env name you made
  
###　On Terminal (again)　　
  pip install -r requirements.txt
  export FLASK_APP=setup.py
  flask run --host=0.0.0.0 --port=8081
  
###　If you get the error "Address already in use"　　
  change the port number
