import flask
application = flask.Flask(__name__)

@application.route('/registration')
def registration():
    return flask.render_template('registration.html')



application.run()