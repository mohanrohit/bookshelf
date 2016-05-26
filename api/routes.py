# routes.py

import views

view_classes = [views.BookView]

def setup_routes(app):
    for view_class in view_classes:
        app.add_url_rule("/hi", view_func = view_class.as_view(""))
