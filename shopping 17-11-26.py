print("====================")
print("Shopping Cart Management System")
print("====================")
items=[]
while True:
    print("Shopping Cart Management System")
    print("1.Add item to cart")
    print("2.View cart")
    print("3.Delete  item")
    print("4.Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        item=input("Enter the item:")
        items.append(item)
        print("Item is added to your cart")
    elif choice=="2":
        if len(items) == 0:
            print("No items are available")
        else:
            for item in items:
                print(item)
    elif choice=="3":
        item=input("Enter the item:")
        if item in items:
            items.remove(item)
            print("Item removed successfully")
        else:
            print("Item not found")
    elif choice=="4":
        print("Thank you for shopping")
        break
    else:
        print("Your choice is invalid")
        
