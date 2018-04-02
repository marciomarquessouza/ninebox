# services/global-data/project/api/models.py

from project import db


class Department(db.Model):
    """Company department or other division"""

    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(4000), nullable=False)
    company_code_01 = db.Column(db.String(255), nullable=False)
    company_code_02 = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, name, description, company_code_01, company_code_02, is_active):
        self.name = name
        self.description = description
        self.company_code_01 = company_code_01
        self.company_code_02 = company_code_02
        self.is_active = is_active
