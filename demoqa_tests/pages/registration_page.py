import os

from demoqa_tests import resource
from selene import browser, have, be


class RegistrationPage:
    def __init__(self):
        self.registration_page_url = '/automation-practice-form'
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.phone_number = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.month_of_birth = browser.element('.react-datepicker__month-select')
        self.year_of_birth = browser.element('.react-datepicker__year-select')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit_button = browser.element('#submit')
        self.subject = browser.element('#subjectsInput')
        self.math_subject = browser.element('.subjects-auto-complete__menu-list').element('//*[text()="Maths"]')
        self.english_subject = browser.element('.subjects-auto-complete__menu-list').element('//*[text()="English"]')
        self.picture_uploader = browser.element('#uploadPicture')

        self.table_student_full_name = browser.element('//table//td[text()="Student Name"]/../td[2]')
        self.table_student_email = browser.element('//table//td[text()="Student Email"]/../td[2]')
        self.table_student_gender = browser.element('//table//td[text()="Gender"]/../td[2]')
        self.table_student_mobile_phone = browser.element('//table//td[text()="Mobile"]/../td[2]')
        self.table_student_date_of_birth = browser.element('//table//td[text()="Date of Birth"]/../td[2]')
        self.table_student_subjects = browser.element('//table//td[text()="Subjects"]/../td[2]')
        self.table_student_hobbies = browser.element('//table//td[text()="Hobbies"]/../td[2]')
        self.table_student_picture = browser.element('//table//td[text()="Picture"]/../td[2]')
        self.table_student_address = browser.element('//table//td[text()="Address"]/../td[2]')
        self.table_student_state_and_city = browser.element('//table//td[text()="State and City"]/../td[2]')

    def open(self):
        browser.open(self.registration_page_url)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        return self

    def fill_first_name(self, value):
        self.first_name.should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.should(be.blank).type(value)
        return self

    def fill_email(self, value):
        self.email.should(be.blank).type(value)
        return self

    def choose_gender(self, gender_name):
        self.gender.element_by(have.value(f'{gender_name}')).element('..').click()
        return self

    def fill_phone_number(self, value):
        self.phone_number.should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth.click()
        self.month_of_birth.type(month)
        self.year_of_birth.type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subject(self, *first_letters):
        for first_letter in first_letters:
            self.subject.type(f'{first_letter}')
            if first_letter == 'm':
                self.math_subject.click()
            if first_letter == 'e':
                self.english_subject.click()
        return self

    def choose_hobby(self, *hobby_numbers):
        for hobby_number in hobby_numbers:
            browser.element(f'label[for="hobbies-checkbox-{hobby_number}"]').click()
        return self

    def upload_picture(self, path):
        self.picture_uploader.set_value(resource.path(path))
        return self

    def fill_current_address(self, value):
        self.address.type(value)
        return self

    def choose_state(self, value):
        self.state.click()
        browser.element(f'//*[text()="{value}"]').click()
        return self

    def choose_city(self, value):
        self.city.click()
        browser.element(f'//*[text()="{value}"]').click()
        return self

    def submit(self):
        self.submit_button.click()
        return self

    def should_have_registered(self, full_name, email, gender, phone_number, date_of_birth,
                               subjects, hobbies, picture, address, state_and_city):
        self.table_student_full_name.should(have.exact_text(full_name))
        self.table_student_email.should(have.exact_text(email))
        self.table_student_gender.should(have.exact_text(gender))
        self.table_student_mobile_phone.should(have.exact_text(phone_number))
        self.table_student_date_of_birth.should(have.exact_text(date_of_birth))
        self.table_student_subjects.should(have.exact_text(subjects))
        self.table_student_hobbies.should(have.exact_text(hobbies))
        self.table_student_picture.should(have.exact_text(picture))
        self.table_student_address.should(have.exact_text(address))
        self.table_student_state_and_city.should(have.exact_text(state_and_city))
        return self
