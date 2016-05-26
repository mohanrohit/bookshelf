from flask import jsonify
from flask.ext.classy import FlaskView

class ApiView(FlaskView):
  def render_error(self, message, code=404):
    return jsonify({"code": code, "message": message}), code

  def render_object(self, object, **kwargs):
    return jsonify({"result": object})
