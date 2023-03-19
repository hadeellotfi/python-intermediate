# Function Arguments: A Recap 
"""
In Python, there are three common types of function arguments:

1. Positional arguments: arguments that are called by their position in the function definition.
2. Keyword arguments: arguments that are called by their name.
3. Default arguments: arguments that are given default values.

To recap, here is what each of these argument types looks like:
"""

# Positional Arguments 
def print_name(first_name, last_name): 
  print(first_name, last_name)
 
print_name('Jiho', 'Baggins') 

# Keyword Arguments 
def print_name(first_name, last_name): 
  print(first_name, last_name)
 
print_name(last_name='Baggins', first_name='Jiho') 


# Default arguments
def print_name(first_name='Jiho', last_name='Baggins'): 
  print(first_name, last_name)
 
print_name() 


# Example : 
"""

Our friend Jiho is trying to get into the restaurant business. 
They asked us to build a simple table assignment program to help manage 
which customer is assigned to each table in the restaurant. 
Jiho wants to store not only the name of the customer for the table but
 also if they hold a VIP status (earned by visiting the restaurant frequently).

Our table information will be stored in a dictionary called tables 
(already defined in our editor) that is structured in the following format:

tablenumber: [name, vip_status]


"""

tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables)

"""
Jiho needs a way to assign new customers to the existing tables
 as they come in for their reservations. Define a new function 
 called assign_table that will take three arguments (in this exact order):

1. table_number
2. name
3. vip_status

Our function assign_table should then use the following arguments to 
assign a new customer to a table in our dictionary tables. 
Use the table_number as the key and a list containing name and vip_status as the value.

"""
# Checkpoint 2 & 5
def assign_table(table_number, name, vip_status=False): 
  tables[table_number] =  [name, vip_status]

"""

Looks like our first reservation just came in!

Call our function assign_table using positional arguments for a customer 
with the name of 'Yoni' to the table 6. Yoni does not have VIP status and 
thus should have the value False.

Optionally, print tables to check that the assignment was successful.
"""
# Checkpoint 3
assign_table(6, 'Yoni', False)
print(tables)

"""
Looks like another customer came in.

Call assign_table using keyword arguments (in any order) to add the new customer
 with the following details:

Name: 'Martha'
Table: 3
VIP Status: True
Make sure to include the keywords in your call to the function!

Optionally, print tables to check that the assignment was successful.
"""
# Checkpoint 4
assign_table(table_number=3, name='Martha', vip_status=True)
print(tables)


"""
# Checkpoint 5
Since most customers are new at the restaurant, we want to use a default value of False for any new table assignment.

Modify the function definition of assign_table and give the parameter vip_status a default value of False.
"""
# Checkpoint 2 & 5
def assign_table(table_number, name, vip_status=False): 
  tables[table_number] =  [name, vip_status]

"""

A new customer just arrived. Add the customer to a table using the following information via positional arguments:

Name: 'Karla'
Table Number: 4
Karla is not a VIP, so we do not need to provide an additional argument since 
we already have a default value of False in our function definition.

Lastly, print the tables dictionary, to see the final table assignments.

"""
# Checkpoint 6
assign_table(4, 'Karla')
print(tables)

