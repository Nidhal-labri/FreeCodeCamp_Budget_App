# This code was made by Nidhal LABRI #
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0

        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
            total += item['amount']

        output = title + items + "Total: " + str(total)
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()


def create_spend_chart(categories):
    category_names = []
    spent_percentages = []
    spent = 0

    for category in categories:
        total_spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total_spent += item['amount']
        spent_percentages.append(round(total_spent, 2))
        spent += round(total_spent, 2)
        category_names.append(category.name)

    spent_percentages = [(percentage / spent) * 100 for percentage in spent_percentages]

    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in spent_percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_name_length = max([len(name) for name in category_names])
    for i in range(max_name_length):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"

    return chart