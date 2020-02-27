import datetime
import os
import sys
import time

coffeeTypes = {1: 'KAFFI', 2: 'CAPPUCCINO', 3: 'LATTE', 4: 'ESPRESSO', 5: 'KAKAO', 8: 'TE'}
TIME = datetime.datetime.now()
CVS_NAME = 'coffee.cvs'


def display_stats():
    with open(CVS_NAME, 'r') as cvsLine:
        date_today = str(TIME).split()[0]
        n_tot = 0
        n_days = 0
        n_cups_today = 0
        prev_cup = 'Y-day'
        prev_date = None
        for c in cvsLine:
            n_tot = n_tot + 1
            date = c.split()[0]
            if date == date_today:
                n_cups_today = n_cups_today + 1
                prev_cup = c.split()[1][:5]
            elif not prev_date == date:
                n_days = n_days + 1
            prev_date = date

        print('\n\n\n____________________________________\n')
        print('Cups total ------------------->\t' + str(n_tot))
        print('Cups average ----------------->\t%.2f' % float(n_tot / n_days))
        print('Cups today ------------------->\t' + str(n_cups_today))
        print('Previous cup was registered -->\t' + prev_cup)
        print('_____________________________________\n\n')


def coffee_exception():
    print('\n\n\n\n\n\n\n\n\n\tNoSuchCoffeeException\n\n\n\n\n\n\n\n\n')
    time.sleep(2)
    sys.exit()


def pad(c_type, padding=13):
    s = ""
    if len(c_type) > 1:
        s = " +1"
    return (str(coffeeTypes.get(int(str(c_type)[0]))) + s).lower().center(padding, ' ')


def success(c_type="1"):
    print("\n\n\n\n\n\n\n\n\n\t    (  )   (   )  )\n" +
          "\t     ) (   )  (  (\n" +
          "\t     ( )  (    ) )\n" +
          "\t     _____________\n" +
          "\t    <_____________> ___\n" +
          "\t    |             |/ _ \\\n" +
          "\t    |" + pad(c_type) + "  | | |\n" +
          "\t    |  registered   |_| |\n" +
          "\t  __|             |\\___/\n" +
          "\t /   \\___________/   \\\n" +
          "\t \\___________________/\n\n\n\n")
    time.sleep(2)
    sys.exit()


def valid_coffee(c_type):
    try:
        int(c_type)
    except ValueError:
        coffee_exception()
    if 1 > len(c_type) or len(c_type) > 2:
        coffee_exception()
    for c in c_type:
        if int(c) not in coffeeTypes:
            return False
    return True


def manual_registration(coffee_cvs):
    print('coffee type:')
    c_type = str(input())
    if not valid_coffee(c_type):
        coffee_exception()
    print('enter time. etc: 0855')
    insert_time = input()
    if len(insert_time) is not 4:
        coffee_exception()
    new_time = TIME.replace(hour=int(insert_time[:2]), minute=int(insert_time[2:]))
    reg_coffee(coffee_cvs, new_time, c_type)


def reg_coffee(coffee_cvs, c_time, c_type):
    coffee_cvs.write(str(c_time) + '\t' + str(c_type) + '\n')
    coffee_cvs.close()
    success(c_type)


if __name__ == "__main__":
    with open(CVS_NAME, 'a') as coffeeCVS:
        display_stats()

        # display options
        print('99:\tmanual registration')
        for c in reversed(sorted(coffeeTypes)):
            print(str(c) + ':\t' + coffeeTypes.get(c))

        coffee_type = input()
        # valid coffeeType?
        if valid_coffee(coffee_type):
            reg_coffee(coffeeCVS, TIME, coffee_type)
        elif int(coffee_type) == 99:
            manual_registration(coffeeCVS)
        elif int(coffee_type) == 69:
            os.system('python coffeeGraph.py')
        else:
            coffee_exception()
