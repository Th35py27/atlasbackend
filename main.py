import threading

# import "packages" from flask
from flask import render_template,request, jsonify  # import render_template from "public" flask libraries
from flask.cli import AppGroup
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Message
from flask_mail import Mail


# import "packages" from "this" project
from __init__ import app, db, cors  # Definitions initialization

<<<<<<< HEAD
# Import necessary modules from the project
from __init__ import app, db
from api.user import user_api
from api.journal import journal_api
from model.journals import initJournals
from api.stats import stats_api
=======

# setup APIs
from api.user import user_api # Blueprint import api definition
from api.player import player_api
from api.searchstocks import search_api
from api.cryptocode import crypto_api
from api.game import game_api
from api.stats import stats_api

# database migrations
from model.users import initUsers
from model.players import initPlayers
#from model.crypto import init_data

# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition

>>>>>>> f1248a294673bef2e816a70d2d4ac5f9ba2826cd

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'torindeanwolff@gmail.com'
app.config['MAIL_PASSWORD'] = 'dslo bpmz hzwv tvnn'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

<<<<<<< HEAD
#class Quote(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    quote_text = db.Column(db.String(255), nullable=False)
#    quote_author = db.Column(db.String(100), nullable=False)
#    user_opinion = db.Column(db.Text, nullable=False)


# Register URIs
app.register_blueprint(user_api)
app.register_blueprint(journal_api)
app.register_blueprint(stats_api)

=======
# register URIs
app.register_blueprint(user_api) # register api routes
app.register_blueprint(player_api)
app.register_blueprint(app_projects) # register app pages
app.register_blueprint(search_api)
app.register_blueprint(crypto_api)
app.register_blueprint(game_api)
app.register_blueprint(stats_api)
>>>>>>> f1248a294673bef2e816a70d2d4ac5f9ba2826cd

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/403/')
def error():
    return render_template('403.html'), 403

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/aws/')  # connects /about/ URL to about() function
def aws():
    return render_template("aws.html")

@app.route('/table/')  # connects /stub/ URL to stub() function
def table():
    return render_template("table.html")

<<<<<<< HEAD
@app.route('/api/users/save_settings', methods=['POST'])  # Define the route for saving settings
def save_settings():
    try:
        # Extract settings data from the request
        settings = request.json.get('settings')

        # Update the user's settings in the database (replace 'current_user' with your actual user object)
        # Example: current_user.update_settings(settings)
        # Make sure to implement this method in your User model

        return jsonify({'message': 'Settings saved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
=======
@app.route('/search/')
def search():
    return render_template("stocksearch.html")

@app.route('/register/', methods=['GET', 'POST'])
def register():
    # Define your site variable here
    site = {'baseurl': 'http://localhost:8086'}

    if request.method == 'POST':
        uid = request.form.get('uid')
        password = request.form.get('password')
        name = request.form.get('name')
        pnum = request.form.get('pnum')
        email = request.form.get('email')
        print(f"uid: {uid}, password: {password}, name: {name}, pnum: {pnum}, email: {email}")

        if not (uid and password and name and pnum and email):
            flash('Please fill out all fields.')
            return redirect(url_for('register'))

        # Check if the email is correctly formatted, else return an error
        if '@' not in email or '.' not in email:
            flash('Please enter a valid email address.')
            return redirect(url_for('register'))

        def send_email(email):
            try:
                msg = Message(
                    'Registration Confirmation',
                    sender='torindeanwolff@gmail.com',
                    recipients=[email]
                )
                msg.body = 'Thank you for registering to Atlas Index!'
                mail.send(msg)
                app.logger.info(f"Email sent successfully to {email}")
            except Exception as e:
                app.logger.error(f"Error sending email to {email}: {str(e)}")


        # Send an email
        send_email(email)

        # Redirect to a success page or do something else as needed
        return redirect(url_for('index'))

    return render_template('register.html', site=site)

@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    # Define your site variable here
    site = {'baseurl': 'http://localhost:8086'}
    return render_template('signin.html', site=site)

@app.route('/help/', methods=['GET', 'POST'])
def help():
    # Define your site variable here
    site = {'baseurl': 'http://localhost:8086'}
    return render_template('help.html', site=site)

@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    # Define your site variable here
    site = {'baseurl': 'http://localhost:8086'}
    return render_template('logout.html', site=site)

@app.route('/profile/', methods=['GET', 'POST'])
def profile():
    # Define your site variable here
    site = {'baseurl': 'http://localhost:8086'}
    return render_template('profile.html', site=site)

@app.route('/display/', methods=['GET'])
def display():
    site = {'baseurl': 'http://localhost:8086'}
    return render_template('getusers.html', site=site)


# @app.route('/display/')
# def display():
#     return render_template("displayusers.html")
>>>>>>> f1248a294673bef2e816a70d2d4ac5f9ba2826cd

@app.before_request
def before_request():
    # Check if the request came from a specific origin
    allowed_origin = request.headers.get('Origin')
<<<<<<< HEAD
    if allowed_origin in ['http://127.0.0.1:4100', 'http://127.0.0.1:4100', 'https://jplip.github.io']:
=======
    if allowed_origin in ['http://localhost:4100', 'http://127.0.0.1:4100', 'https://nighthawkcoders.github.io', 'http://localhost:8086']:
>>>>>>> f1248a294673bef2e816a70d2d4ac5f9ba2826cd
        cors._origins = allowed_origin
        
# Create an AppGroup for custom commands
custom_cli = AppGroup('custom', help='Custom commands')

# Define a command to generate data
@custom_cli.command('generate_data')
def generate_data():
    #initUsers()
    initJournals()


# Register the custom command group with the Flask application
app.cli.add_command(custom_cli)

# Run the application on the development server
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port="8086")