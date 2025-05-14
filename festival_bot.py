import datetime
import time
from plyer import notification

# Festival list
festival_list = {
    "Diwali": "29-10",
    "Christmas": "25-12",
    "Holi": "17-03",
    "New Year": "01-01",
    "Eid": "10-04",
    "Bakrid": "17-06",
    "Raksha Bandhan": "19-08",
    "Durga Puja": "10-10",
    "Ganesh Chaturthi": "07-09",
    "Navratri": "03-10",
    "Shivaratri": "26-02",
    "Independence Day": "15-08",
    "Republic Day": "26-01",
    "Gandhi Jayanti": "02-10",
    "Janmashtami": "26-08",
}

def check_today(date_today):
    found = False
    print("\n----- Festival Check -----")
    for fest_name, fest_date in festival_list.items():
        if fest_date == date_today:
            send_notification(fest_name)
            found = True
        elif is_coming_soon(fest_date, date_today):
            send_notification(fest_name, soon=True)
            found = True
    if not found:
        print("No festivals today or in the next 3 days.")
    print("-----------------------------\n")

def is_coming_soon(fest_date, today_date):
    today = datetime.datetime.strptime(f"{today_date}-2024", "%d-%m-%Y")
    fest = datetime.datetime.strptime(f"{fest_date}-2024", "%d-%m-%Y")
    gap = (fest - today).days
    return 0 < gap <= 3

def send_notification(name, soon=False):
    title = "Festival Reminder"
    msg = f"{name} is coming soon!" if soon else f"Today is {name}!"
    print(f">> {msg}")
    try:
        notification.notify(
            title=title,
            message=msg,
            timeout=10
        )
    except:
        print("Notification failed.")

def add_festival():
    print("\n--- Add or Update Festival ---")
    name = input("Enter festival name : ").strip()
    date = input("Enter festival date (dd-mm): ").strip()
    try:
        datetime.datetime.strptime(f"{date}-2024", "%d-%m-%Y")
        festival_list[name] = date
        print(f"Festival '{name}' has been added/updated.")
    except ValueError:
        print("Invalid date! Please use dd-mm format.")
    print("-------------------------------\n")

def run_every_day():
    while True:
        today = datetime.datetime.now().strftime("%d-%m")
        check_today(today)
        time.sleep(86400)


if __name__ == "__main__":
    while True:
        print(" ")
        print("====================================")  # To make the output look visibly pleasing
        print("        Festival Reminder Bot       ")
        print("====================================")
        print("1. Show Festivals")
        print("2. Add Festival")
        print("3. Check Today")
        print("4. Exit")
        print(" ")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            print("\n------ Festival List ------")
            for name, date in festival_list.items():
                print(f"{name:<20} : {date}")
            print("-------------------------------\n")
        elif choice == '2':
            add_festival()
        elif choice == '3':
            today = datetime.datetime.now().strftime("%d-%m")
            print(f"Today is: {today}")
            check_today(today)
        elif choice == '4':
            print("\nHave a great day!")
            break
        else:
            print("Invalid option. Please try again.\n")