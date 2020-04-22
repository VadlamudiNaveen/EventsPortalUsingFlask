from flask import render_template, session, request, url_for, redirect, flash
from app import app, redis_client
from flask_mail import Mail, Message


@app.route('/')
def index():
    if 'username' in session and redis_client['username']:
        return render_template('index.html')
    return render_template('index.html')


@app.route('/account')
def account():
    from app import mongo
    get_1 = mongo.db.stories
    get_post = list(get_1.find({'email': session['username']}))
    if len(get_post) == 0:
        flash("NO POSTS YET TRY TO ADD SOME CRAZY STORIES YAR !")
    return render_template('stories.html', data=get_post)


@app.route('/logout')
def logout():
    session.pop('username')
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    from app import mongo
    import bcrypt
    import datetime
    users = mongo.db.users
    log = users.find_one({'name': request.form['username']})
    print(log)
    pass_word = redis_client.__getitem__(request.form['username'])
    if pass_word is not None:
        if bcrypt.checkpw(request.form['pass0'].encode('utf-8'), pass_word):
            session['username'] = request.form['username']
            if users.update_one({"name": log['name']}, {"$set": {"updated_at": datetime.datetime.utcnow()}}):
                print(log['updated_at'])
            mail = Mail(app)
            try:
               with app.app_context():
                  with mail.connect() as conn:
                      message = 'Hello everyone how are you i hope every one are fine and thop.. happy UGADI...'
                      subject = "hello, %s" % 'girebos726@emailnube.com'
                      msg = Message(recipients=['girebos726@emailnube.com'], body=message, subject=subject)
                      print(1)
                      conn.send(msg)
            except Exception as e:
                      return (str(e))
            return redirect(url_for('account'))
        return "Invalid username or password"
    return "User is not registered yet"


@app.route('/register', methods=['POST', 'GET'])
def register():
    from app import mongo
    import bcrypt
    import datetime
    import flask
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})
        if existing_user is None:
            if request.form['pass2'] == request.form['pass1']:
                hpass = bcrypt.hashpw(request.form['pass1'].encode('utf-8'), bcrypt.gensalt())
                redis_client.__setitem__(request.form['username'], hpass)
                users.insert(
                    {'name': request.form['username'], 'password': hpass, 'created_at': datetime.datetime.now,
                     'sys_info': flask.request.user_agent.string, 'updated_at': datetime.datetime.utcnow()})

                return redirect(url_for('index'))
            return flash('Passwords Doesnt match', 'warning')
        return flash('The username already exists', 'warning')


# time O(n) documents and O(m) space
@app.route('/fresher', methods=['GET'])
def fresher():
    from app import mongo
    data = []
    fresher = mongo.db.freshers
    temp = fresher.find().sort('_id')
    for i in temp:
        data.append(i)
    print(data)
    return render_template('jobs.html', data=data)


# time O(n) documents and O(m) space
@app.route('/experience', methods=['GET'])
def experience():
    from app import mongo
    data = []
    experience = mongo.db.experience
    temp = experience.find().sort('_id')
    for i in temp:
        data.append(i)
    print(data)
    return render_template('jobs.html', data=data)


# time O(n) documents
@app.route('/stories', methods=['GET'])
def stories():
    from app import mongo
    data = []
    stories = mongo.db.stories
    temp = stories.find().sort('published_at')
    for i in temp:
        data.append(i)
    return render_template('stories.html', data=data)


# time taken for the module to fetch the html page as it creates an object and O(n) time for processing as it uses
# tree data structure space is Dictionary..
@app.route('/events', methods=['GET'])
def events():
    events = {}
    import requests
    from bs4 import BeautifulSoup
    url = "https://www.meetup.com/find/events/?allMeetups=true&radius=50&userFreeform=Chennai%2C+India&mcId=c1018094&mcName=Chennai%2C+IN&eventFilter=mysugg"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(class_="event-listing-container")
    for result in results:
        link = result.find_next('a')['href']
        name = result.find_next(itemprop="name")
        events[name.text] = link
        # time = result.find_next(itemprop="startDate")
        # count = result.find_next(class_="attendee-count")
    print(events)
    # redis_client["list_of_events"] = json.dumps(events)
    return render_template('events.html', events=events)


@app.route('/trending', methods=['GET'])
def trending():
    pass
