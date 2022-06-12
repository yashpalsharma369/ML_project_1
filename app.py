from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return "<h>Updated title for Machine learning project to test CI CD pipeline</h>"

if __name__=="__main__":
    app.run(debug=True)