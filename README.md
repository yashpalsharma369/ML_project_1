# ML_project_1
This is a sample ML project

# Step 1: Create github repo

# Step 2: Create a project folder and clone the git  repo into the folder

# Step 3: Open VS Code IDE
'''
code .
'''

# Creating virtual environment venv
'''
conda create -p venv python==3.7 -y
'''

# Step 5: Activate virtual environment
'''
conda activate venv/
'''

# Step 6: Create requirements.txt file
'''
pip install -r requirements.txt

# 7: Create the flask app in app.py

# 8: Add exceptions within gitignore - for the venv folder 

# 9: Add file to git
'''
git add <filename> OR
git add .
git status 
git log
git commit -m message
git push origin main --> to send version/changes to git
git remote -v --> to check remote url
git branch
git revert
git diff
'''

# 10: Post committing changes on GIT, we need to setup CI/CD pipeline in Heroku
'''
HEROKU_EMAIL = yashurockslife@gmail.com
HEROKU_API_KEY = f3402b22-4935-4205-b825-4c5a4cd7a752
HEROKU_APP_NAME = ml-regressor-proj369

# 11: BUILD DOCKER IMAGE
'''
docker build -t <image_name>:<tag_name> .
NOTE: image_name should be in lowercase
'''

To list docker image
'''
docker images
'''
Run docker image
'''
docker run -p 5000:5000 -e PORT=5000 <<IMAGE_ID>>

To list running containers 
'''
docker ps
'''

Stop docker containers
'''
docker stop <<container_id>>
'''
# 12: Create .github/workflows/main.yaml file - this file will instruct 