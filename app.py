import json
from flask import Flask, render_template, Response, request, url_for, redirect
from forms import LoginForm, SignupForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '6d2759031f072b955fe8e502e6ca8283'

@app.route('/login')
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        message = json.dumps({'username': form.username.data})
        return redirect(url_for('home', message=message))
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    userData = {"username":form.username.data, "password": form.password.data}
    if form.validate_on_submit():
        with open('./authorizedUsers.json', 'r') as f:
            jsonFormat = f.read()                          # read from the file  
            dataDecionary = json.loads(jsonFormat)         # convert to python dictionary
            dataDecionary[form.username.data] = userData   # append to the dictionary
            jsonFormat = json.dumps(dataDecionary)         # convert the dictionary back to json format
        
        with open('./authorizedUsers.json', 'w') as f:
            json.dump(jsonFormat, f)
        message = json.dumps({'username': form.username.data})
        return redirect(url_for('home', message=message))
    return render_template('signup.html', form=form)

@app.route('/home')
def home():
    message = json.loads(request.args['message']) # get username data from the login page
    username = message['username']
    with open('./posts.json', 'r') as f:
        posts = f.read()
    userPosts = json.loads(posts)[username]  
    result = sorted(userPosts, key=lambda x: datetime.strptime(x['time'], '%Y-%m-%dT%H:%M:%SZ')) # sort user post in a chronological order
    return render_template('home.html', username = username, posts=result)

@app.route('/users')
def users():
    username = request.args.get('username')
    message = json.dumps({'username': username})
    with open('./users.json', 'r') as f:
        users = f.read()
    print(users)
    followers = json.loads(users)
    print(followers)
    return render_template('users.html', users=followers, username=username, message=message)

@app.route('/posts')
def posts_view():
    with open('./posts.json', 'r') as f:
        posts = f.read()
    return Response(posts, mimetype="application/json")

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)