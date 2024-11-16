import allure

from demoqa_tests import resource
from selene import browser, have, be

from demoqa_tests.data.users import User


class RegistrationPage:
    def __init__(self):
        self.registration_page_url = '/automation-practice-form'

        self.first_name_input = browser.element('#firstName')
        self.last_name_input = browser.element('#lastName')
        self.email_input = browser.element('#userEmail')
        self.gender_picker = browser.all('[name=gender]')
        self.phone_number_input = browser.element('#userNumber')
        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.month_of_birth = browser.element('.react-datepicker__month-select')
        self.year_of_birth = browser.element('.react-datepicker__year-select')
        self.address_input = browser.element('#currentAddress')
        self.state_input = browser.element('#state')
        self.city_input = browser.element('#city')
        self.submit_button = browser.element('#submit')
        self.subject_input = browser.element('#subjectsInput')
        self.subject_picker = browser.element(".subjects-auto-complete__menu-list")
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

    @allure.step('Open registration form')
    def open(self):
        browser.open(self.registration_page_url)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        return self

    @allure.step('Fill the user registration form and submit result')
    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.choose_gender(user.gender)
        self.fill_phone_number(user.phone_number)
        self.fill_date_of_birth(user.date_of_birth['year'], user.date_of_birth['month'], user.date_of_birth['day'])
        self.fill_subjects(user.subjects)
        self.choose_hobbies(user.hobbies)
        self.upload_picture(user.upload_file_name)
        self.fill_current_address(user.current_address)
        self.choose_state(user.state)
        self.choose_city(user.city)
        self.submit()

    @allure.step('Fill first name')
    def fill_first_name(self, value):
        self.first_name_input.should(be.blank).type(value)
        return self

    @allure.step('Fill last name')
    def fill_last_name(self, value):
        self.last_name_input.should(be.blank).type(value)
        return self

    @allure.step('Fill email')
    def fill_email(self, value):
        self.email_input.should(be.blank).type(value)
        return self

    @allure.step('Fill gender')
    def choose_gender(self, gender_name):
        self.gender_picker.element_by(have.value(f'{gender_name}')).element('..').click()
        return self

    @allure.step('Fill phone_number')
    def fill_phone_number(self, value):
        self.phone_number_input.should(be.blank).type(value)
        return self

    @allure.step('Fill birthday')
    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth_input.click()
        self.month_of_birth.type(month)
        self.year_of_birth.type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    @allure.step('Fill subjects')
    def fill_subjects(self, student_subjects: tuple):
        for student_subject in student_subjects:
            self.subject_input.type(student_subject[0].lower())
            self.subject_picker.element(f"//*[text()='{student_subject}']").click()
        return self

    @allure.step('Fill hobbies')
    def choose_hobbies(self, student_hobbies: dict):
        for key, value in student_hobbies.items():
            browser.element(f'label[for="hobbies-checkbox-{value}"]').click()
        return self

    @allure.step('Upload picture')
    def upload_picture(self, path: str):
        self.picture_uploader.set_value(resource.path(path))
        return self

    @allure.step('Fill current_address')
    def fill_current_address(self, value):
        self.address_input.type(value)
        return self

    @allure.step('Fill state')
    def choose_state(self, value):
        self.state_input.click()
        browser.element(f'//*[text()="{value}"]').click()
        return self

    @allure.step('Choose city')
    def choose_city(self, value):
        self.city_input.click()
        browser.element(f'//*[text()="{value}"]').click()
        return self

    @allure.step('Submit form')
    def submit(self):
        self.submit_button.click()
        return self

    @allure.step('User should be registered with his data')
    def should_registered_user_with(self, user: User):

        full_name = user.first_name + ' ' + user.last_name
        birthday = user.date_of_birth['day'] + ' ' + user.date_of_birth['month'] + ',' + user.date_of_birth['year']
        subjects = ', '.join(map(str, user.subjects))
        hobbies = ', '.join(map(str, user.hobbies))
        state_and_city = user.state + ' ' + user.city

        self.table_student_full_name.should(have.exact_text(full_name))
        self.table_student_email.should(have.exact_text(user.email))
        self.table_student_gender.should(have.exact_text(user.gender))
        self.table_student_mobile_phone.should(have.exact_text(user.phone_number))
        self.table_student_date_of_birth.should(have.exact_text(birthday))
        self.table_student_subjects.should(have.exact_text(subjects))
        self.table_student_hobbies.should(have.exact_text(hobbies))
        self.table_student_picture.should(have.exact_text(user.upload_file_name))
        self.table_student_address.should(have.exact_text(user.current_address))
        self.table_student_state_and_city.should(have.exact_text(state_and_city))

        return self
