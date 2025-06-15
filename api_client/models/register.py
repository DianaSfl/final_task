from faker import Faker
fake = Faker()
class RegisterModel:
    @staticmethod
    def random():
        return {"login": fake.user_name(), "password": "Password"}