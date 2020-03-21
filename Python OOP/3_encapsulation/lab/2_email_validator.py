class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        return len(name) >= self.min_length

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def get_email_data(self, email):
        at = email.index('@')
        period = email.index('.')

        return [
            email.split('@')[0],
            email[at + 1: period],
            email.split('.')[1]
        ]

    def validate(self, email):

        name, mail, domain = self.get_email_data(email)

        if self.__validate_name(name) is False:
            return False

        if self.__validate_mail(mail) is False:
            return False

        if self.__validate_domain(domain) is False:
            return False

        return True


# tests below
mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
