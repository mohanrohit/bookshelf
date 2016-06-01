﻿# model.py

from api import db

class ModelMixin(object):
  def save(self):
    db.session.add(self)
    db.session.commit()
