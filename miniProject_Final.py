class Supermarket:
    """This class contains some basic methods---
     1. Insert_item() : to insert items in the supermarket.
     2. Buy_items() : for selecting the items from the supermarket to buy.
     3. Show_cart() : to show the selected items.
     4. Discount() : to show the discount if applicable for the purchase.
     5. Bill() : to show the bill."""


    # item stock in store = { 'item name' : [ stock quantity , item price ]}
    __stock = {'chips': [100, 10], 'soap': [20, 25], 'juice': [50, 60]}

    def __init__(self):
        self.greet()
        self.item_list = []
        self.quantity_list = []
        self.final_value = 0
        self.discount = 0
        self.bill_list = ""

    def end_task(self):
        user_input = int(input("Enter 1 to continue , or Enter 0 to Exit: "))
        if user_input == 0:
            return False
        else:
            return True

    def menu(self):

        option = int(input("Enter your desired option: "))

        if option == 1:
            self.Insert_item()

        elif option == 2:
            self.Buy_item()

        elif option == 3:
            self.Show_cart()

        elif option == 4:
            self.Discount()

        elif option == 5:
            self.Bill()

        else:
            print("Thank You! Visit Us Again.")
            exit()

    def Insert_item(self):
        print("\n::::: Add Items :::::\n")
        temp = True
        while temp == True:

            item_name = input("item name: ")

            while True:
                try:
                    item_detail = []
                    item_detail.append(int(input("Quantity: ")))
                    item_detail.append(int(input("Price: ")))
                    break
                except ValueError:
                    print("Quantity and Price should be in digits !!")

            Supermarket.__stock[item_name] = item_detail

            print("Item Added Successfully.")
            temp = self.end_task()

    def Buy_item(self):
        a = 1
        temp = True

        print("\n::: Buy Items ::: \n-------Item List-------")

        for i in Supermarket.__stock:
            print(f"Item {a} : {i}, Price: {Supermarket.__stock[i][1]}")
            a += 1
        while temp == True:
            number = int(input("Enter item number: "))
            quantity = int(input("Enter Quantity: "))
            self.item_list.append(number)
            self.quantity_list.append(quantity)
            temp = self.end_task()

    def Show_cart(self):
        if len(self.item_list) == 0:
            print("Cart is empty !")
        else:
            p = 1
            print("\n::: Cart :::\n")

            for i in self.item_list:

                keyVar = list(Supermarket.__stock)[i - 1]
                quantVar = self.quantity_list[p - 1]
                finalQuant = Supermarket.__stock[keyVar][0]
                finalQuant -= quantVar

                if finalQuant < 0:
                    print(f"{p}. {keyVar} is out of stock")
                else:
                    Supermarket.__stock[keyVar][0] = finalQuant
                    print(f"{p}. {keyVar} * {quantVar}")

                    self.bill_list = self.bill_list + "\n" + f"{keyVar} * {quantVar} = {Supermarket.__stock[keyVar][1] * quantVar}"
                    self.final_value = self.final_value + quantVar * Supermarket.__stock[keyVar][1]

                p += 1

    def Discount(self):
        if self.final_value > 1999:
            self.discount = (self.final_value * (10 / 100))
        else:
            self.discount = 0
        print(f"\n::: Discount:::\n{self.discount}")

    def Bill(self):
        print(f"\n::: Bill :::\n{self.bill_list}\n -----------------")
        print(f"Total Amount : {self.final_value - self.discount}")

    @staticmethod
    def greet():
        print(''':::::: Welcome to ABC Super Market ::::::
              \nEnter 1 : Insert Item
              \nEnter 2 : Buy Item
              \nEnter 3 : Show Cart
              \nEnter 4 :Show discount
              \nEnter 5 :Generate Bill
              \nEnter 6 :Exit\n''')


if __name__ == '__main__':
    mt = Supermarket()
    mt.menu()
    mt.Show_cart()
    mt.Discount()
    mt.Bill()
