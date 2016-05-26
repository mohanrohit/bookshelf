import os

import sys

import re
import inflect
import importlib

class Router(object):
  def __init__(self, app, views_path = os.path.dirname(__file__) + "/views", models_path = os.path.dirname(__file__) + "/models"):
    sys.path.append(views_path)
    sys.path.append(models_path)

    self.inflect = inflect.engine()
    self.inflect.classical()

    self.views_path = views_path
    self.models_path = models_path

    self.app = app
    self.views = {}
    self.setup()

  def setup(self):
    self._import_models()
    self._import_views()
    self._add_routes()

    for rule in self.app.url_map.iter_rules():
      print rule, rule.defaults, rule.arguments, rule.endpoint

  def _get_names_from_files(self, files_path, file_name_pattern):
    all_files = os.listdir(files_path)

    files_regex = re.compile(file_name_pattern, re.IGNORECASE)
    matching_files = filter(files_regex.search, all_files)

    object_names = map(lambda f: os.path.splitext(f)[0], matching_files)

    return object_names

  def _get_view_class_name(self, view_name):
    view_base_name = view_name.split("_")[0]
    view_class_name = view_base_name.lower().capitalize() + "View"

    return view_class_name

  def _import_views(self):
    view_names = self._get_names_from_files(self.views_path, "view\.py$")

    views = {view_name: self._get_view_class_name(view_name) for view_name in view_names}

    for view_name, view_class_name in views.items():
      view_class = importlib.import_module(view_name).__getattribute__(view_class_name)

      self.views[view_class_name] = view_class

  def _get_model_class_name(self, model_name):
    return model_name.lower().capitalize()

  def _import_models(self):
    model_names = self._get_names_from_files(self.views_path, "\.py$")

    models = {model_name: model_name.lower().capitalize() for model_name in model_names}

    for model_name, model_class_name in models.items():
      if model_name == "__init__":
        continue

      importlib.import_module(model_name)

  def _add_routes(self):
    # once views and models are imported, then add the routes
    # to the views
    for view_class_name, view_class in self.views.items():
      view_base_name = view_class_name[:-len("View")].lower()

      singular_base_name = self.inflect.singular_noun(view_base_name)
      if singular_base_name == False: # already singular
        view_base_name = self.inflect.plural_noun(view_base_name)
      else:
        view_base_name = self.inflect.plural_noun(singular_base_name)

      view_class.register(self.app, route_base=view_base_name, trailing_slash=False)
