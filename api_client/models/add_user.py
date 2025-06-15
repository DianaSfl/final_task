from faker import Faker

fake = Faker('ru_RU')


class AddUserModel:
    @staticmethod
    def random():
        return {
            "name": fake.first_name(),
            "age": fake.random_int(min=1, max=100),
            "gender": fake.random_element(elements=("М", "Ж")),
            "data_birth": fake.date_of_birth(minimum_age=1, maximum_age=100).strftime("%d.%m.%Y"),
            "active": fake.boolean()
        }
