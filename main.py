import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user = "root",
  password = "root",
  database = "store",
)

cursor = mydb.cursor()

while True:
    cursor.execute("SELECT * FROM product;")
    display = cursor.fetchall()
    for product in display:
        print(f"ID: {product[0]}, Name: {product[1]}, Description: {product[2]}, Price: {product[3]}, Quantity: {product[4]}, Category ID: {product[5]}")

    choice = input("Please (a)dd a product, (m)odify a product, (d)elete a product, (e)xport to CSV or (q)uit: ")
    match choice.lower():
        case "a" | "add":
            name = input("Enter product name: ")
            description = input("Enter product description: ")
            price = int(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            id_category = int(input("Enter product category's number: "))

            cursor.execute(f"INSERT INTO product (name, description, price, quantity, id_category) VALUES ('{name}', '{description}', {price}, {quantity}, {id_category})")
            mydb.commit()

            print("Product added successfully")
        case "m" | "modify":
            id = int(input("Enter product id: "))

            cursor.execute(f"SELECT * FROM product WHERE id = {id}")
            product = cursor.fetchone()
            print(f"Selected product: {product}")
            
            name = input("Enter product new name: ")
            description = input("Enter product new description: ")
            price = int(input("Enter product new price: "))
            quantity = int(input("Enter product new quantity: "))
            id_category = int(input("Enter product new category's number: "))

            cursor.execute(f"UPDATE product SET name = '{name}', description = '{description}', price = {price}, quantity = {quantity}, id_category = {id_category} WHERE id = {id}")
            mydb.commit()

            print("Product modified successfully")
        case "d" | "delete":
            id = int(input("Enter product id: "))

            cursor.execute(f"DELETE FROM product WHERE id = {id}")
            mydb.commit()
            
            print("Product deleted successfully")
        case "e" | "export":
            with open('products.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Description", "Price", "Quantity", "Category ID"])
                cursor.execute("SELECT * FROM product;")
                display = cursor.fetchall()
                for product in display:
                    writer.writerow(product)
            print("Data exported successfully")
        case _:
            break