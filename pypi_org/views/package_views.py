import flask


blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
def package_details(package_name: str):
    return "Package details for {}".format(package_name)

@blueprint.route('/project/<package_name>')
def package_details(package_name: str):
    return "Package details for {}".format(package_name)

