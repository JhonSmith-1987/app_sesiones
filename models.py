from app import db

class Direccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(250))
    password = db.Column(db.String(250))
    confirm_password = db.Column(db.String(250))

    def __str__(self):
        return (
            f'id: {self.id}, '
            f'user: {self.user}, '
            f'password: {self.password}, '
            f'confirm_password: {self.confirm_password}'
        )
