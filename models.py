from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    """Model for Pets in database for adoption."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Provide image of pet ."""
        return self.photo_url or "https://i.chzbgr.com/full/9028930816/h5BB62E4E/profile-silhouette-of-a-cat-for-facebook-of-a-really-lazy-looking-cat"


def connect_db(app):
    """Connect database to Flask application"""

    db.app = app
    db.init_app(app)