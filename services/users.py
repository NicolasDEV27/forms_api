from models.users import User as UserModel
from schemas.forms import User

class UserService():

    def __init__(self, db) -> None:
        self.db = db

    def get_users(self):
        result = self.db.query(UserModel).all()
        return result

    def get_user(self, name):
        result = self.db.query(UserModel).filter(UserModel.Name == name).first()
        return result

    def create_user(self, user: User):
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return 