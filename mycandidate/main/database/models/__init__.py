from main.app import db
from main.database.models.config import Config
from main.database.models.candidates import get_data

# Minimal Candidate model for API and testing
class Candidate(db.Model):
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ward_id = db.Column(db.Integer, nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ward_id": self.ward_id,
        }
