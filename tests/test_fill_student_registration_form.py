
from demoqa_tests.data.users import student_1
from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_fill_student_registration_form_and_check_pop_up():
    """
    Автотест на полное заполнение и отправку формы https://demoqa.com/automation-practice-form
    и проверку заполненных данных в поп-апе
    """
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(student_1)
    registration_page.should_registered_user_with(student_1)
