
from system.core.router import routes

routes['default_controller'] = 'Notes'
routes['POST']['/notes/create'] = 'Notes#create'
routes['POST']['/notes/update'] = 'Notes#update'
routes['POST']['/notes/delete'] = 'Notes#delete'
