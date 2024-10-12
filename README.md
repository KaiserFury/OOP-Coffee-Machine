Here’s a `README.md` for your Coffee Machine program using the Object-Oriented Programming (OOP) concept:

---

# Coffee Machine Program

This program simulates a coffee machine using the principles of Object-Oriented Programming (OOP). It allows users to select drinks, check resources, process transactions, and dispense coffee while managing resources such as water, milk, and coffee beans.

## Features
- Offers three drink options: **espresso**, **latte**, and **cappuccino**.
- Maintains a report of current resource levels (water, milk, coffee, and money).
- Processes coin transactions and handles insufficient payments.
- Dispenses drinks if enough resources are available and transaction is successful.
- Allows the machine to be turned off with a secret command.

## Requirements
The program uses a command-line interface to interact with the user.

1. **Drink Selection**:  
   Users are prompted with the following:
   ```
   What would you like? (espresso/latte/cappuccino):
   ```
   The user can enter a choice or use commands like `off` or `report`.

2. **Turn Off the Machine**:  
   Entering `off` turns off the machine, ending the program.

3. **Report Functionality**:  
   Entering `report` generates a report showing current resource levels (e.g., water, milk, coffee, and money).

4. **Resource Management**:  
   The program checks if enough resources are available to make the selected drink. If not, it prints an error message (e.g., "Sorry, there is not enough water.") and prompts the user again.

5. **Transaction Processing**:  
   The program calculates the monetary value of inserted coins (quarters, dimes, nickels, and pennies) and checks if the amount is sufficient for the selected drink.

6. **Refunds and Change**:  
   If the inserted money is insufficient, it refunds the user. If the user inserts extra money, the machine returns the change rounded to two decimal places.

7. **Dispensing Drinks**:  
   Once the transaction is successful and there are enough resources, the program deducts the required ingredients and dispenses the drink (e.g., "Here is your latte. Enjoy!").

## How to Use
1. Run the program in your terminal.
2. Follow the on-screen prompts to:
   - Select a drink.
   - Insert the required amount of money.
   - Receive your drink if the transaction is successful.
   - Check the machine's resource report or turn off the machine.

## Class Structure
The program follows the OOP paradigm with the following key components:
- **CoffeeMachine**: Manages the main functionality of the machine, including resources and user interactions.
- **Menu**: Handles the available drink options and their ingredient requirements.
- **MoneyHandler**: Processes the money transactions, including coin insertion, total calculation, and change handling.

## Example Output
```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 5
How many nickels?: 0
How many pennies?: 0
Here is $0.50 dollars in change.
Here is your latte. Enjoy!
```

## Dependencies
No external libraries are required for this program. It runs on any Python environment with basic functionality.

## Future Improvements
- Add more drink options.
- Implement graphical user interface (GUI) support.
- Add customization options (e.g., sugar levels, milk types).

---
