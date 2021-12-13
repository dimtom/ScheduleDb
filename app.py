import flask
import os
import schedules


# create a new flask application
app = flask.Flask(__name__)

# initialization: load all schedules to dictionary
data_directory = os.path.join(app.root_path, 'data')
schedules.all_schedules = schedules.loadAllSchedules(data_directory)


@app.route("/")
def handler_main():
    return flask.render_template("index.html", base_url=flask.request.base_url)


@app.route("/health", methods=['GET'])
def handler_health():
    response = flask.make_response("Health status: OK")
    return response, 200


@app.route("/schedule", methods=['GET'])
def handler_allSchedules():
    ids = schedules.findAllSchedules()

    response = {"schedules": ids}
    return response


@app.route("/schedule/<id>", methods=['GET'])
def handler_getSchedule(id):
    if id not in schedules.all_schedules:
        flask.abort(404)
        return

    mode = flask.request.args.get("mode", "json")
    mode = mode.lower()

    response = None
    if mode == "json":
        response = flask.make_response(schedules.getJsonSchedule(id), 200)
        response.mimetype = "application/json"
    elif mode == "mwt":
        response = flask.make_response(schedules.getMwtSchedule(id), 200)
        response.mimetype = "text/plain"
    elif mode == "log":
        response = flask.make_response(schedules.getLogSchedule(id), 200)
        response.mimetype = "text/plain"
    else:
        flask.abort(
            400, "Invalid mode value. Valid values are: json | mwt | log.")
    return response


@app.route("/find")
def handler_find():
    numPlayers = flask.request.args.get("players", 0)
    numTables = flask.request.args.get("tables", 0)
    numAttempts = flask.request.args.get("distance", 0)

    try:
        configuration = {
            "numPlayers": int(numPlayers),
            "numTables": int(numTables),
            "numAttempts": int(numAttempts)
        }
    except ValueError:
        flask.abort(400)

    ids = schedules.findSchedules(configuration)
    response = {"schedules": ids}
    return response


'''
@app.route("/schedule/upload", methods=['POST'])
def handler_uploadSchedule():
    # @app.route('/upload', methods=['GET', 'POST'])
    # f = request.files['the_file']
    # f.save('/var/www/uploads/uploaded_file.txt')
    response = flask.make_response()
    return response, 501  # not implemented
'''
