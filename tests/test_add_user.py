import pytest
import logging

logger = logging.getLogger("add_user_tests")


class TestAddUser:
    def test_add_user_valid_data(self, auth_admin, add_user_page, default_user_data):
        user_data = default_user_data
        add_user_page.add_user(
            name_text=user_data["name"],
            age_text=user_data["age"],
            gender_text=user_data["gender"],
            data_birth_text=user_data["data_birth"],
            active_check=user_data["active"]
        )
        result = add_user_page.get_result_text()
        logger.info(f"Result: {result}")
        assert "Пользователь успешно добавлен!" in result, f"Пользователь не был добавлен"

    def test_add_user_empty_name(self, auth_admin, add_user_page, default_user_data):
        user_data = default_user_data.copy()
        user_data["name"] = ""
        add_user_page.add_user(
            name_text=user_data["name"],
            age_text=user_data["age"],
            gender_text=user_data["gender"],
            data_birth_text=user_data["data_birth"],
            active_check=user_data["active"]
        )
        result = add_user_page.get_empty_name_text()
        logger.info(f"Result: {result}")
        assert "Поле обязательно" in result, f'Пользователь добавлен с пустым полем "имя"'

    def test_add_user_empty_age(self, auth_admin, add_user_page, default_user_data):
        user_data = default_user_data.copy()
        user_data["age"] = None
        add_user_page.add_user(
            name_text=user_data["name"],
            age_text=user_data["age"],
            gender_text=user_data["gender"],
            data_birth_text=user_data["data_birth"],
            active_check=user_data["active"]
        )
        result = add_user_page.get_empty_age_text()
        logger.info(f"Result: {result}")
        assert "Поле обязательно" in result, f'Пользователь добавлен с пустым полем "возраст"'

    @pytest.mark.xfail(reason="Баг: пол не валидируется как обязательное поле")
    def test_add_user_empty_gender(self, auth_admin, add_user_page, default_user_data):
        user_data = default_user_data.copy()
        user_data["gender"] = None
        add_user_page.add_user(
            name_text=user_data["name"],
            age_text=user_data["age"],
            gender_text=user_data["gender"],
            data_birth_text=user_data["data_birth"],
            active_check=user_data["active"]
        )
        result = add_user_page.get_result_text()
        logger.info(f"Result: {result}")
        assert "Пользователь успешно добавлен!" not in result, f"Пользователь был добавлен  без обязательного поля 'пол'"

    @pytest.mark.xfail(reason="Баг: отрицательный возраст не валидируется")
    def test_add_user_negative_age(self, auth_admin, add_user_page, default_user_data):
        user_data = default_user_data.copy()
        user_data["age"] = -1
        add_user_page.add_user(
            name_text=user_data["name"],
            age_text=user_data["age"],
            gender_text=user_data["gender"],
            data_birth_text=user_data["data_birth"],
            active_check=user_data["active"]
        )
        result = add_user_page.get_result_text()
        logger.info(f"Result: {result}")
        assert "Пользователь успешно добавлен!" not in result, f"Пользователь был добавлен c отрицательным числом в поле 'возраст'"

    @pytest.mark.xfail(reason="Баг: числа в имени не валидируются")
    def test_add_user_number_is_name(self, auth_admin, add_user_page, default_user_data):
        user_data = default_user_data.copy()
        user_data["name"] = 123
        add_user_page.add_user(
            name_text=user_data["name"],
            age_text=user_data["age"],
            gender_text=user_data["gender"],
            data_birth_text=user_data["data_birth"],
            active_check=user_data["active"]
        )
        result = add_user_page.get_result_text()
        logger.info(f"Result: {result}")
        assert "Пользователь успешно добавлен!" not in result, f"Пользователь был добавлен c числами в поле 'имя'"

    @pytest.mark.xfail(reason="Баг: пол не валидируется")
    def test_add_user_invalid_gender(self, auth_admin, add_user_page, default_user_data):
        user_data = default_user_data.copy()
        user_data["gender"] = "не_пол"
        add_user_page.add_user(
            name_text=user_data["name"],
            age_text=user_data["age"],
            gender_text=user_data["gender"],
            data_birth_text=user_data["data_birth"],
            active_check=user_data["active"]
        )
        result = add_user_page.get_result_text()
        logger.info(f"Result: {result}")
        assert "Пользователь успешно добавлен!" not in result, f"Пользователь был добавлен с невалидными данными в 'пол'"

    def test_add_user_without_logging_in(self, add_user_page, default_user_data):
        user_data = default_user_data.copy()
        add_user_page.add_user(
            name_text=user_data["name"],
            age_text=user_data["age"],
            gender_text=user_data["gender"],
            data_birth_text=user_data["data_birth"],
            active_check=user_data["active"]
        )
        result = add_user_page.get_result_text()
        logger.info(f"Result: {result}")
        assert "Вы не авторизованы. Пожалуйста, войдите в систему." in result, f"Пользователь был добавлен с невалидными данными в 'пол'"

