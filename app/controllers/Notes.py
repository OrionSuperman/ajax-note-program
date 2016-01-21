"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Notes(Controller):
    def __init__(self, action):
        super(Notes, self).__init__(action)
        self.load_model('Note')
        
    def index(self):
        notes = self.models['Note'].all()
        return self.load_view('index.html', notes=notes)

    def index_html(self):
        notes = self.models['Note'].all()
        return self.load_view('/partials/notes.html', notes=notes)

    def create(self):
        new_note = {
            'title' : request.form['title']
        }
        self.models['Note'].create(new_note)
        notes = self.models['Note'].all()
        return self.load_view('/partials/notes.html', notes=notes)

    def update(self):
        print "HIT"
        print request.form
        print "HIT 2"
        note_update = {
            'description' : request.form['description'],
            'title' : request.form['title'],
            'id' : request.form['id']
        }
        print note_update
        self.models['Note'].update(note_update)
        notes = self.models['Note'].all()
        return self.load_view('/partials/notes.html', notes=notes)

    def delete(self):
        self.models['Note'].delete(request.form['id'])
        notes = self.models['Note'].all()
        return self.load_view('/partials/notes.html', notes=notes)

