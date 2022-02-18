class Customer:
    def __init__(self, name, address, creditcard):
        self.name = name
        self.address = address
        self.__creditcard = creditcard
        
    def get_creditcard(self):
        return self.__creditcard
        
    def set_creditcard(self, creditcard):
        self.__creditcard = creditcard
        
    def print_info(self):
        print("customer name: ", self.name)
        print("customer address: ", self.address)
        print("credit card (last four): ", str(self.__creditcard)[-4:])
        
        
customer1 = Customer("andy", "123 happy st", 1234432112344321 )
customer1.print_info()



customer1.set_creditcard(4321123443211234)
print("new cc number: ", customer1.get_creditcard())
print(customer1.__creditcard) # this wont work
