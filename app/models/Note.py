""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Note(Model):
    def __init__(self):
        super(Note, self).__init__()

    def all(self):
        query = "SELECT * FROM notes"
        return self.db.query_db(query)

    def create(self, new_note):
        query = "INSERT INTO notes (title, created_at, updated_at) VALUES (%s, NOW(), NOW())"
        data = [new_note['title']]
        return self.db.query_db(query, data)

    def update(self, note_update):
        query = "UPDATE notes SET title=%s, description=%s, updated_at=NOW() WHERE id=%s"
        data = [note_update['title'], note_update['description'], note_update['id']]
        print query
        print data
        self.db.query_db(query, data)

    def delete(self, id):
        query = "DELETE FROM notes WHERE id=%s"
        data = [id]
        self.db.query_db(query,data)

    """
    Below is an example of a model method that queries the database for all users in a fictitious application

    def get_all_users(self):
        print self.db.query_db("SELECT * FROM users")

    Every model has access to the "self.db.query_db" method which allows you to interact with the database
    """

    """
    If you have enabled the ORM you have access to typical ORM style methods.
    See the SQLAlchemy Documentation for more information on what types of commands you can run.
    """
