import flask
import os
import schedules


# create a new flask application
app = flask.Flask(__name__)

# initialization: load all schedules to dictionary
data_directory = os.path.join(app.root_path, 'data')
schedules.load_all_schedules(data_directory)


@app.route("/")
def handler_main():
    return flask.render_template("index.html", base_url=flask.request.base_url)


@app.route("/health", methods=['GET'])
def handler_health():
    response = flask.make_response("Health status: OK")
    return response, 200


@app.route("/schedule", methods=['GET'])
def handler_allSchedules():
    ids = [id for id in schedules.all_schedules.keys()]
    response = {"schedules": ids}
    return response


@app.route("/schedule/<id>", methods=['GET'])
def handler_getSchedule(id):
    if id in schedules.all_schedules:
        return schedules.all_schedules[id]
    else:
        flask.abort(404)


'''
TODO: add in future
'''

'''
@app.route("/find")
def handler_search():
    # request.args:
    # request.get_json()
    response = flask.make_response()
    return response, 400  # bad request


@app.route("/schedule/upload", methods=['POST'])
def handler_uploadSchedule():
    # @app.route('/upload', methods=['GET', 'POST'])
    # f = request.files['the_file']
    # f.save('/var/www/uploads/uploaded_file.txt')
    response = flask.make_response()
    return response, 501  # not implemented
'''
