import random
from datetime import date

QUOTES = [
    "Discipline beats motivation.",
    "Small progress every day adds up.",
    "You don’t have to be perfect — just consistent.",
    "Future you is watching. Make them proud.",
    "Start now. Not tomorrow.",
    "Hard work compounds."
]

FILE_NAME = "weekly_goals.txt"


def get_goals():
    while True:
        try:
            n = int(input("How many goals this week? (3–5): "))
            if 3 <= n <= 5:
                break
        except:
            pass
        print("Enter a number between 3 and 5.")

    goals = []
    for i in range(n):
        g = input(f"Enter goal #{i+1}: ")
        goals.append({"text": g, "done": False})

    return goals


def save_goals(goals):
    quote = random.choice(QUOTES)
    today = date.today()

    with open(FILE_NAME, "w") as f:
        f.write("WEEKLY GOALS GAME\n")
        f.write(f"Date: {today}\n\n")
        f.write(f"Motivation: \"{quote}\"\n\n")

        for i, g in enumerate(goals, 1):
            box = "[x]" if g["done"] else "[ ]"
            f.write(f"{i}. {box} {g['text']}\n")


def load_goals():
    goals = []
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                if line.strip().startswith(tuple(str(i) for i in range(1, 10))):
                    parts = line.strip().split(" ", 2)
                    done = parts[1] == "[x]"
                    text = parts[2]
                    goals.append({"text": text, "done": done})
    except FileNotFoundError:
        return None
    return goals


def show_goals(goals):
    print("\nYour Goals:")
    for i, g in enumerate(goals, 1):
        box = "✅" if g["done"] else "⬜"
        print(f"{i}. {box} {g['text']}")


def mark_done(goals):
    show_goals(goals)
    try:
        choice = int(input("Mark which goal done? (number): "))
        if 1 <= choice <= len(goals):
            goals[choice - 1]["done"] = True
            print("Nice work! Goal completed 💪")
    except:
        print("Invalid input.")


def main():
    print("=== Weekly Goals Game ===")

    goals = load_goals()

    if not goals:
        goals = get_goals()
        save_goals(goals)
        print("Goals saved!\n")

    while True:
        show_goals(goals)
        print("\nMenu:")
        print("1 — Mark goal done")
        print("2 — Save & Exit")

        cmd = input("Choose: ")

        if cmd == "1":
            mark_done(goals)
            save_goals(goals)
        elif cmd == "2":
            save_goals(goals)
            print("Progress saved. See you tomorrow.")
            break


if __name__ == "__main__":
    main()
