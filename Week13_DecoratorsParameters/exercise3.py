from datetime import date
from datetime import datetime


class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def _get_age_of_years(self, today):
        return today.year - self.date_of_birth.year

    def _get_age_with_months(self, today, years):
        if (today.month, today.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day,
        ):
            years -= 1
        return years

    @property
    def age(self):
        today = date.today()
        years = self._get_age_of_years(today)
        years = self._get_age_with_months(today, years)
        return years


def is_user(user):
    if not isinstance(user, User):
        raise TypeError("The first parameter must be a User instance")
    return True


def is_adult(user):
    if user.age < 18:
        raise PermissionError("The user is not an adult")
    return True


def validate_adult(func):
    def wrapper(user: User, *args, **kwargs):
        is_user(user)
        is_adult(user)
        return func(user, *args, **kwargs)

    return wrapper


@validate_adult
def access_bar(user: User):
    return f"Access to bar granted user aged {user.age}."


@validate_adult
def buy_alcohol(user: User):
    return f"Alcohol purchase allowed for user aged {user.age}."


def main():
    # Example users
    adult_user = User(date_of_birth=date(1990, 5, 15))
    minor_user = User(date_of_birth=date(2010, 8, 22))

    # Test with adult user
    try:
        print(access_bar(adult_user))
        print(buy_alcohol(adult_user))
    except Exception as e:
        print(f"Error: {e}")

    # Test with minor user
    try:
        print(access_bar(minor_user))
    except Exception as e:
        print(f"Error: {e}")

    try:
        print(buy_alcohol(minor_user))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
