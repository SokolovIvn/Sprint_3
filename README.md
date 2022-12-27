Sprint 3

/tests - Лежат все тесты по файлам
conftest.py - активация драйвера

Locators.py - локаторы
user_data.py - генерация логина, пароля, email 

файлы с тестами:
test_constructor.py     - тесты на конструктор
    - test_goto_constructor_with_personal_account - Переход из личного кабинета в конструктор
    - test_check_section_topping_is_selected - переход в раздел Начинки
    - test_check_section_saucec_is_selected - переход в раздел Соусы
    - test_check_section_buns_is_selected - переход в раздел Булки

test_login.py           - тесты на логин
    - test_login_with_button_through_on_main - вход по кнопке «Войти в аккаунт» на главной 
    - test_login_through_button_header - вход через кнопку «Личный кабинет»
    - test_login_through_button_on_register_page - вход через кнопку в форме регистрации
    - test_login_through_button_on_page_forgot_password - вход через кнопку в форме восстановления пароля

test_personal_account.py- тесты на личный кабинет
    - test_log_out_personal_account - выход из лк
    - test_login_go_to_lk_through_header - Переход в личный кабинет

test_registration.py    - тесты на регистрацию
    - test_geristration_full - полный позитивный тест на регистрацию
    - test_registration_bad_pswd_check_fail_text_done - проверка информера ввода некорректного пароля

 