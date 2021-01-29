import csv
import datetime
import json
import time

import requests

log_file_path = str(datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")) + ".log"
account_file_path = "data/lifter-data_social-instagram.csv"
accounts_left_path = "results/accounts_left"
positive_result_path = "results/working_accounts"
negative_result_path = "results/defunct_accounts"

session = requests.Session()
with open("headers") as fp:
    session.headers.update(
        json.load(fp)
    )


def load_accounts():
    try:
        with open(account_file_path, encoding="UTF-8") as csvfile:
            reader = csv.reader(csvfile)
            data = [row[1] for row in reader]
            data.pop(0)  # first element is column header, so "Instagram"
            return data
    except IOError as error:
        log("Error reading file: {}".format(error))
        return None
    except BaseException as error:
        log("Error loading accounts: {}".format(error))
        return None


def check_account(instagram: str) -> int:
    response = session.get("https://www.instagram.com/{}/?__a=1".format(instagram))
    return response.status_code


def check_accounts(accs: []) -> None:
    while len(
            accs) > 0:  # doing this instead of for-each for greater control over iteration - we might check accounts multiple times
        log("Checking: {}".format(accs[0]))
        result = check_account(accs[0])
        log("Result code: {}".format(result))
        if result == 200:  # account exists
            log("Found account {}. Adding to working accounts and moving on in 1 second..".format(accs[0]))
            update_results(accs, accs[0], True)
            accs.pop(0)
            time.sleep(1)
        elif result == 404:  # account dead
            log("Account {} does not exist. Adding to dead accounts and moving on in 1 second..".format(accs[0]))
            update_results(accs, accs[0], False)
            accs.pop(0)
            time.sleep(1)
        else:  # unknown error. Probably rate limiter or instagram figured out you're pretending to be a browser
            log("Unknown error with status code {}. Waiting for 2 minutes and trying again.".format(str(result)))
            time.sleep(2 * 60)


def update_results(accs, current_acc, result):
    try:
        with open(positive_result_path if result else negative_result_path, mode="a") as result_file:
            result_file.write("{},\n".format(current_acc))
        with open(accounts_left_path, mode="w") as left_file:
            accs_csv = ""
            for acc in accs[1:]:
                accs_csv += "dummy,{}\n".format(acc)
            left_file.write(accs_csv)
    except IOError as error:
        log("Error reading file: {}".format(error))
        return None
    except BaseException as error:
        log("Error logging results: {}".format(error))
        return None


def log(message):
    try:
        with open(log_file_path, mode="a", encoding="UTF-8") as log_file:
            to_write = "{}: {}\n".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), message)
            log_file.write(to_write)
            print(to_write)
    except BaseException as error:
        print("Error with logging. Good luck with that. {}".format(error))


if __name__ == "__main__":
    log("Loading accounts..")
    accounts = load_accounts()
    log("Loaded accounts. Start checking..")
    check_accounts(accounts)
    log("Checking done. Finishing..")
