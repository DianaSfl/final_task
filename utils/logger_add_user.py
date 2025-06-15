import logging

logger = logging.getLogger("add_user_tests")

def log_data_add_user(user_data: dict, result: str):
    name = user_data["name"]
    age = user_data["age"]
    gender = user_data["gender"]
    birthday = user_data["data_birth"]
    active = user_data["active"]

    logger.info(f'name: {name}, age: {age}, gender: {gender}, birthday: {birthday}, active: {active}')
    logger.info(f'result: {result}')