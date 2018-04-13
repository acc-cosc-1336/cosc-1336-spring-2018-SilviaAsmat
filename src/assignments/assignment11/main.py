from src.assignments.assignment11.invoice import Invoice
from src.assignments.assignment11.invoice_item import InvoiceItem
from src.assignments.assignment11.product import Product
from src.assignments.assignment11.customer import Customer
from src.assignments.assignment11.average_customer import AverageCustomer
from src.assignments.assignment11.good_customer import GoodCustomer
#Write import statements for classes AverageCustomer and GoodCustomer


'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object ASSIGNMENT10: Make sure to change invoice bill_to argument to an instance of a Customer class 

In the loop:
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    ASSIGNMENT10: Create a product object and add description and cost as parameter arguments.  Quantity remains same.
    Create a new InvoiceItem, use the newly created product as a parameter argument 
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''


invoice1 = Invoice(Customer('Customer', 'Smith', '5121234567'), '03012018')
#see invoice creation above to complete next two statements
#ASSIGNMENT 11: Create an invoice instance named invoice2, with parameter instance of an Average Customer
invoice2 = Invoice(AverageCustomer('Customer', 'Smith', '5121234567'), '03012018')
#ASSIGNMENT 11: Create an invoice instance named invoice3, with parameter instance of an Good Customer
invoice3 = Invoice(GoodCustomer('Customer', 'Smith', '5121234567'), '03012018')
keep_going = 'y'

while keep_going == 'y':

    description = input("Enter description: ")
    quantity = int(input("Enter quantity: "))
    cost = float(input("Enter cost: "))

    invoice1.add_invoice_item(InvoiceItem(Product(1, description, cost), quantity))
    #see statement above to complete next two statements
    #ASSIGNMENT 11: add an invoice item to invoice 2 object with exact same Invoice item as invoice2 above
    invoice2.add_invoice_item(InvoiceItem(Product(1, description, cost), quantity))
    #ASSIGNMENT 11: add an invoice item to invoice 3 object with exact same Invoice item as invoice3 above
    invoice3.add_invoice_item(InvoiceItem(Product(1, description, cost), quantity))
    keep_going = input("Enter another type y: ")


print(invoice1.get_invoice_total())
print()
#ASSIGNMENT11: call get invoice total method of invoice2 object
print(invoice2.get_invoice_total())
print()
#ASSIGNMENT11: call get invoice total method of invoice3 object
print(invoice3.get_invoice_total())
print()

invoice1.print_invoice()
invoice2.print_invoice()
invoice3.print_invoice()
#ASSIGNMENT 11: call print invoice method of invoice 2 object
#ASSIGNMENT 11: call print invoice method of invoice 3 object




