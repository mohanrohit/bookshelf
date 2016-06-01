from collections import defaultdict

from flask import jsonify, request
from flask.ext.classy import FlaskView

class ApiView(FlaskView):
  def __init__(self):
    self.params = defaultdict(lambda: None)

  def before_request(self, name, *args, **kwargs):
    self.params.update(request.values)
    self.params.update(kwargs)
    if request.json:
      self.params.update(request.json)

  def render_error(self, message, code=404):
    return jsonify({"code": code, "message": message}), code

  def render_object(self, object, **kwargs):
    print "in render_object"
    print object
    return jsonify({"result": object})
