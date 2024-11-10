import os

from selene import browser, have, be

from demoqa_tests.pages.registration_page import RegistrationPage


def test_fill_student_registration_form_and_check_pop_up():
    """
    Автотест на полное заполнение и отправку формы https://demoqa.com/automation-practice-form
    и проверку заполненных данных в поп-апе
    """
    registration_page = RegistrationPage()

    registration_page.open()
    (
        registration_page
        .fill_first_name('Alexander')
        .fill_last_name('Ivanov')
        .fill_email('maily-mail@sb.ru')
        .choose_gender('Female')
        .fill_phone_number('9645120774')
        .fill_date_of_birth('1997', 'April', '12')
        .fill_subject('m', 'e')
        .choose_hobby('1', '3')
        .upload_picture('SI.jpg')
        .fill_current_address('Moscow, Red Square, h. 1')
        .choose_state('Haryana')
        .choose_city('Karnal')
        .submit()
    )
    registration_page.should_have_registered('Alexander Ivanov',
                                             'maily-mail@sb.ru',
                                             'Female',
                                             '9645120774',
                                             '12 April,1997',
                                             'Maths, English',
                                             'Sports, Music',
                                             'SI.jpg',
                                             'Moscow, Red Square, h. 1',
                                             'Haryana Karnal'
                                             )
