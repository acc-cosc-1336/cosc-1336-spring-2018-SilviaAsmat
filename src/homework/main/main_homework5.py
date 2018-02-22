from src.homework.homework5 import write_sales_data
from src.homework.homework5 import read_sales_data
#write the import statements for homework5 functions

#With the functions created in homework5...
#Prompt user for number of sales records to input.
#Open a file for text writing.
#Iterate and prompt user for item name and price.
#Save item name and price to file in one line
#Calculate sum of price and write to file
#Calculate average price and write to file


def main():
    sales_records = int(input('Enter number of sales records: '))
    file_object = open('data.txt', 'w')
    file_object.write('Item\tPrice\n')
    total_price = 0

    for i in range(0,sales_records):
        item_name = input('Enter item name')
        item_price = float(input('Enter item price'))
        write_sales_data(file_object,item_name,item_price)
        total_price += item_price
    avg_price = total_price / sales_records
    file_object.write('Total'+'\t'+str(total_price)+'\n')
    file_object.write('Avg Price'+'\t'+str(avg_price))


#Open a file for text reading.
#Read the saved file and output table
file_object = open('data.txt', 'r')
read_sales_data(file_object)

