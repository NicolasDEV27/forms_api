from models.users import User as UserModel
from schemas.forms import User

class UserService():


    def __init__(self, db) -> None:
        self.db = db

    def get_users(self):
        result = self.db.query(UserModel).all()
        return result

    def get_user_name(self, name):
        result = self.db.query(UserModel).filter(UserModel.Name == name).first()
        return result

    def get_user_DNI(self, dni: int):
        result = self.db.query(UserModel).filter(UserModel.DNI == dni).first()
        return result

    def create_user(self, user: User):
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return 

    def update_user(self, dni: int, data: User):
        user = self.db.query(UserModel).filter(UserModel.DNI == dni).first()
        user.Name = data.Name
        user.Last_names = data.Last_names
        user.Age = data.Age
        user.Height = data.Height
        user.Birthday = data.Birthday
        user.email = data.email
        user.password = data.password
        self.db.commit()
        return

    def delete_user(self, dni: int):
        less_user = self.get_user_DNI(dni)
        self.db.delete(less_user)
        self.db.commit()
        return 