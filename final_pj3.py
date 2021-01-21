class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount,  f'Transfer to {other_category.category}')
            other_category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        title = f'{self.category:*^30}\n'
        body = ''
        total = 0
        for item in self.ledger:
            body += item["description"][:23].ljust(23) + str(
                '{:.2f}'.format(item["amount"]))[:7].rjust(7) + '\n'
            total += item["amount"]
        table = title + body + f'Total: {total:.2f}'
        return table


def create_spend_chart(categories):
    total_spent = 0
    longest = ''  # Queria saber longitud de la palabra mas larga para luego iterar por renglon
    for category in categories:
        category.spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total_spent += abs(item["amount"])
                category.spent += abs(item["amount"])
    #     print(f'\nCategory ledger for {category.category} is : {category.ledger}\nAnd that category spent is {category.spent}')
    # print(f'\n\nTotal spent is {total_spent}\n')
    for category in categories:
        category.percentage = int(category.spent / total_spent * 100)
        if len(category.category) > len(longest):  # Word printing purposes
            longest = category.category
    chart = 'Percentage spent by category\n'
    for i in range(100, -1, -10):
        chart += f'{i:>3}| '
        for category in categories:
            if i <= category.percentage:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
    width = len(categories) * 3 + 1
    chart += '    ' + '-' * width + '\n'
    for i in range(len(longest)):
        chart += '     '
        for category in categories:
            try:
                chart += category.category[i] + '  '
            except:
                chart += '   '
        chart += '\n'
    chart = chart[:-1]
    return chart

################################## TEST 1 ######################################
# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print(food) #Gasta 76.04
# print(clothing) #Gasta 25.55
# print(auto) #Gasta 15 Tot gstado 116.59

# print(create_spend_chart([food, clothing, auto]))
