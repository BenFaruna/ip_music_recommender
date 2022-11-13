'''reload model for session on startup'''
from models.engine import Storage

storage = Storage()
storage.reload()