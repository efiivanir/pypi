import flask


blueprint = flask.Blueprint('acount', __name__, template_folder='templates')


@blueprint.route('/acount')
def index():
    return flask.render_template('account/index.html')

            ## REGISTER
@blueprint.route('/account/register', method = ['GET'])
def register_get():
    return flask.render_template('account/register.html')

@blueprint.route('/account/register', method = ['PUT'])
def register_put():
    return flask.render_template('account/register.html')

            ## LOGIN
@blueprint.route('/account/login', method = ['GET'])
def login_get():
    return flask.render_template('account/login.html')

@blueprint.route('/account/login', method = ['PUT'])
def login_put():
    return flask.render_template('account/login.html')

            ## LOGOUT
@blueprint.route('/account/logout')
def logout():
    return flask.render_template('account/logout.html')


