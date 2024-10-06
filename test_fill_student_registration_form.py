import os

from selene import browser, have, be


def test_fill_student_registration_form_and_check_pop_up():
    """
    Автотест на полное заполнение и отправку формы https://demoqa.com/automation-practice-form
    и проверку заполненных данных в поп-апе
    """
    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('Alexander')
    browser.element('#lastName').should(be.blank).type('Ivanov')
    browser.element('#userEmail').should(be.blank).type('maily-mail@sb.ru')
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('9645120774')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select > option[value="1997"]').click()
    browser.element('.react-datepicker__month-select > option[value="3"]').click()
    browser.element('.react-datepicker__day--012').click()
    browser.element('#subjectsInput').type('m')
    browser.element('.subjects-auto-complete__menu-list').element('//*[text()="Maths"]').click()
    browser.element('#subjectsInput').type('e')
    browser.element('.subjects-auto-complete__menu-list').element('//*[text()="English"]').click()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath("SI.jpg"))
    browser.element('#currentAddress').type('Moscow, Red Square, h. 1')
    browser.element('#state').click()
    browser.element('//*[text()="Haryana"]').click()
    browser.element('#city').click()
    browser.element('//*[text()="Karnal"]').click()
    browser.element('#submit').click()

    browser.element('//table//td[text()="Student Name"]/../td[2]').should(have.exact_text("Alexander Ivanov"))
    browser.element('//table//td[text()="Student Email"]/../td[2]').should(have.exact_text("maily-mail@sb.ru"))
    browser.element('//table//td[text()="Gender"]/../td[2]').should(have.exact_text("Female"))
    browser.element('//table//td[text()="Mobile"]/../td[2]').should(have.exact_text("9645120774"))
    browser.element('//table//td[text()="Date of Birth"]/../td[2]').should(have.exact_text("12 April,1997"))
    browser.element('//table//td[text()="Subjects"]/../td[2]').should(have.exact_text("Maths, English"))
    browser.element('//table//td[text()="Hobbies"]/../td[2]').should(have.exact_text("Sports, Music"))
    browser.element('//table//td[text()="Picture"]/../td[2]').should(have.exact_text("SI.jpg"))
    browser.element('//table//td[text()="Address"]/../td[2]').should(have.exact_text("Moscow, Red Square, h. 1"))
    browser.element('//table//td[text()="State and City"]/../td[2]').should(have.exact_text("Haryana Karnal"))

