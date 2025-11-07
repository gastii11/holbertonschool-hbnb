from app import create_app
from app.extensions import db
from app.services.facade import HBnBFacade

app = create_app()

with app.app_context():
    db.create_all()
    facade = HBnBFacade()

if __name__ == '__main__':
    app.run(debug=True)
