import logging

logger = logging.getLogger("add_user_tests")

def log_data_add_user(name_text, age_text, gender_text, data_birth_text, active_check):
    name = name_text
    age = age_text
    gender = gender_text
    birthday = data_birth_text
    active = active_check

    logger.info(f'name: {name}, age: {age}, gender: {gender}, birthday: {birthday}, active: {active}')