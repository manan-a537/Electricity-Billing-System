from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy instance
db = SQLAlchemy()

class Reading(db.Model):
    """Model for storing meter readings"""
    __tablename__ = 'readings'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    consumption = db.Column(db.Float, nullable=False)  # in kWh
    peak_demand = db.Column(db.Float, nullable=False)  # in kW
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp.isoformat(),
            'consumption': self.consumption,
            'peak_demand': self.peak_demand,
            'created_at': self.created_at.isoformat()
        }

class Bill(db.Model):
    """Model for storing monthly bills"""
    __tablename__ = 'bills'

    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(20), nullable=False)  # e.g., "January"
    year = db.Column(db.Integer, nullable=False)
    consumption = db.Column(db.Float, nullable=False)  # Total monthly consumption
    peak_demand = db.Column(db.Float, nullable=False)  # Highest demand in the month
    amount = db.Column(db.Float, nullable=False)  # Total bill amount
    due_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'month': self.month,
            'year': self.year,
            'consumption': self.consumption,
            'peak_demand': self.peak_demand,
            'amount': self.amount,
            'due_date': self.due_date.isoformat(),
            'created_at': self.created_at.isoformat()
        }

class ConsumptionHistory(db.Model):
    """Model for storing consumption history"""
    __tablename__ = 'consumption_history'

    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    consumption = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'month': self.month,
            'year': self.year,
            'consumption': self.consumption,
            'amount': self.amount,
            'created_at': self.created_at.isoformat()
        }

class Alert(db.Model):
    """Model for storing usage alerts"""
    __tablename__ = 'alerts'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'message': self.message,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active
        }

def init_db(app):
    """Initialize the database"""
    db.init_app(app)
    
    # Create all tables
    with app.app_context():
        db.create_all()