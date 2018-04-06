#Write import statements for classes invoice and invoice_item and PRODUCT
from src.assignments.assignment10.invoice import  Invoice
from src.assignments.assignment10.invoice_item import  InvoiceItem
from src.assignments.assignment10.customer import Customer
from src.assignments.assignment10.product import Product
#ASSIGNMENT10 Write import statements for classes product and customer


'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object 

In the loop:
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    Create a new InvoiceItem, use the newly created product as a parameter argument 
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''
#ASSIGNMENT10: Make sure to change invoice bill_to argument to an instance of a Customer class
customer = Customer('Silvia', 'Asmat', '1234567890')
invoice = Invoice(customer, '03012018')

keep_going = 'y'

while keep_going == 'y':

    description = input("Enter description: ")
    quantity = int(input("Enter quantity: "))
    cost = float(input("Enter cost: "))
    product_id = input("Enter product ID: ")

    #ASSIGNMENT10: Create a product object and add description and cost as parameter arguments.
    #Quantity parameter remains same.
    product = Product(product_id, cost, description)
    invoice.add_invoice_item(InvoiceItem(quantity, product))

    keep_going = input("Enter another type y: ")


invoice.print_invoice()




