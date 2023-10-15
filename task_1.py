# Homework-1 >>> def get_birthdays_per_week
import calendar
from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):
    birthdays_by_weekday = defaultdict(list)
    current_date = datetime.today().date()
    current_weekday = current_date.weekday()
    first_weekday_name = calendar.day_name[0]
    res_list, res_str = [], ""
    for user in users:
        user_name = user["name"]
        user_birthday = user["birthday"].date()
        birthday_this_year = user_birthday.replace(year=current_date.year)
        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(
                year=birthday_this_year.year + 1)
        delta_days = (birthday_this_year - current_date).days
        if delta_days < 7:
            birthday_weekday = birthday_this_year.weekday()
            birthday_weekday_name = calendar.day_name[birthday_weekday]
            # виклик у неділю:
            if current_weekday == 6:
                if birthday_weekday == 6:       # іменинників поточної НД переносимо на ПН
                    birthdays_by_weekday[first_weekday_name].append(user_name)
                elif birthday_weekday != 5:     # іменинники ПН-ПТ у свої дні, іменинників наступної СБ не виводимо у цей тиждень
                    birthdays_by_weekday[birthday_weekday_name].append(
                        user_name)
            # виклик у понеділок:
            elif current_weekday == 0:
                if birthday_weekday < 5:        # іменинники ПН-ПТ у свої дні, іменинників наступної СБ-НД не виводимо у цей тиждень
                    birthdays_by_weekday[birthday_weekday_name].append(
                        user_name)
            # виклик у інші дні:
            else:
                if birthday_weekday < 5:        # іменинники ПН-ПТ у свої дні
                    birthdays_by_weekday[birthday_weekday_name].append(
                        user_name)
                else:                           # іменинників СБ-НД переносимо на ПН
                    birthdays_by_weekday[first_weekday_name].append(user_name)
    for k, v in birthdays_by_weekday.items():
        res_list.append(k + ": " + (", ").join(v))
    res_str = ("\n").join(res_list)
    return print(res_str)


# тестовий словник
users = [{"name": "Ivan Golovko", "birthday": datetime(1955, 10, 13)},
         {"name": "Petro Nechiy", "birthday": datetime(1962, 10, 14)},
         {"name": "Maria Kvitkova", "birthday": datetime(1960, 10, 15)},
         {"name": "Andre Tan", "birthday": datetime(1963, 10, 16)},
         {"name": "Anton Patron", "birthday": datetime(1974, 10, 17)},
         {"name": "Marina Ptushkina", "birthday": datetime(1980, 10, 17)},
         {"name": "Daria Ivanova", "birthday": datetime(1982, 10, 18)},
         {"name": "Tomas Gates", "birthday": datetime(1984, 10, 19)},
         {"name": "Dmytro Kashko", "birthday": datetime(1957, 10, 19)},
         {"name": "Maksim Kalistro", "birthday": datetime(1959, 10, 20)},
         {"name": "Natali Petrucho", "birthday": datetime(1964, 10, 21)},
         {"name": "Olga Solomko", "birthday": datetime(1965, 10, 22)},
         {"name": "Svetlana Kuzub", "birthday": datetime(1979, 10, 23)}
         ]

# перевірка роботи функції
get_birthdays_per_week(users)
