melon_cost = 1.00


def counting_payments(filename):
    '''Takes file, reads it, takes values and counts if customer underpaid'''
    file = open(filename)  # opens txt file
    for line in file:  # loops through each file line
        line = line.rstrip().split("|")  # removes whitespace on the right
        customer_name = line[1]  # second item on the line defined as variable
        customer_melons = line[2]  # third item on the line defined as variable
        customer_paid = line[3]  # fourth item on the line defined as variable
        customer_expected = int(customer_melons) * \
            float(melon_cost)  # counting expected payment
        if customer_expected != customer_paid:  # checks if expected payment is not equal to paid
            print(
                f"{customer_name} paid ${customer_paid}, expected ${customer_expected}")  # prints out f string with results
    file.close()  # closes file


# calls function with text file name as an argument
counting_payments("customer-orders.txt")
