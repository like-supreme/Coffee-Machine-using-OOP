# ☕ Python Coffee Machine — OOP Version

This is the **Object-Oriented Programming (OOP)** version of a terminal-based coffee machine simulation written in Python. It improves upon the procedural version by encapsulating logic into reusable and scalable classes.

---

## 🚀 Features

- Class-based design for `Menu`, `CoffeeMaker`, and `MoneyMachine`
- Choose from `espresso`, `latte`, and `cappuccino`
- Simulates coin input (quarters, dimes, nickels, pennies)
- Checks ingredient availability
- Calculates profit and gives change
- Displays resource and money report
- Can be shut down using the `"off"` command

---

## 🧱 Classes Used

| Class         | Description                                |
|---------------|--------------------------------------------|
| `MenuItem`     | Represents a drink with ingredients & cost |
| `Menu`         | Contains available drinks and lookup logic |
| `CoffeeMaker`  | Handles resource tracking & coffee making  |
| `MoneyMachine` | Manages coin input and transaction logic   |

---

## 📁 Project Structure

oop_coffee_machine/
├── main.py # Main app loop
├── coffee_maker.py # CoffeeMaker class
├── money_machiene.py # MoneyMachine class
├── menu.py # Menu and MenuItem classes

---

## ▶️ Example Usage

What would you like? latte/espresso/cappuccino/: latte
Please insert coins.
How many quarters?: 10
How many dimes?: 4
...
Here is $1.42 in change.
Here is your latte ☕️. Enjoy!

---

## 📚 Learning Outcomes

- Object-Oriented Design in Python
- Class abstraction and encapsulation
- Clean module separation and reusability
- Conditionals, loops, and input handling

---

## 💡 Bonus Ideas

- Add maintenance mode or refill mode
- Expand to GUI (e.g. Tkinter, PyQt)
- Save profit and stock to file (persistence)

---

## 🙋‍♂️ Author

Developed by Like-Supreme (only the main.py)  
This is the **OOP version** of the Coffee Machine project.  
See also: [Procedural Version Repo](https://github.com/like-supreme/Coffee-Machine.git) 
# Coffee-Machine-using-OOP
☕ Coffee Machine Simulation in Python using Object-Oriented Programming. Includes menu management, resource tracking, and coin-based transactions.
