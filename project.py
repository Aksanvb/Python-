import qrcode   #generates qr
import os      #opens qr image based on os
import platform  #opens qr image based on os
import time     #adds delay to simulate payment
import uuid   #generates unique transaction id
import webbrowser   #opens upi link in default browser
from datetime import datetime  #captures current date and time for billing and transaction naming 

#menu card details created
menu = {
    1: {"item": "Dosa", "price": 120},
    2: {"item": "Gravy", "price": 250},
    3: {"item": "Idly", "price": 80},
    4: {"item": "Coffee", "price": 60},
    5: {"item": "Ice Cream", "price": 90}
}

def show_menu():    #menu is displayed
    print("\n🍴 Welcome to Sanjay's Restaurant 🍴")
    print("------------ MENU ------------")
    for key, value in menu.items():
        print(f"{key}. {value['item']} - ₹{value['price']}")
    print("------------------------------")

def open_image(file_path):   #opens qr image 
    system = platform.system()
    try:
        if system == "Windows":
            os.startfile(file_path)
        elif system == "Darwin":  # macOS
            os.system(f"open \"{file_path}\"")
        else:  # Linux
            os.system(f"xdg-open \"{file_path}\"")
    except Exception as e:
        print(f"⚠ Could not open QR automatically: {e}")

def generate_qr(total_amount, upi_id):   #constructs upi payment details,payment and time delay
    payee_name = "Sanjay Restaurant"
    tr = str(uuid.uuid4()).replace("-", "")[:20]
    tn = f"Order_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    am = f"{total_amount:.2f}"

    upi_uri = f"upi://pay?pa={upi_id}&pn={payee_name.replace(' ', '+')}&am={am}&cu=INR&tn={tn}&tr={tr}"

    # Generate QR code
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(upi_uri)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    file_name = f"payment_qr_{tr}.png"
    img.save(file_name)
    print("\n✅ QR Code generated successfully!")
    print(f"📁 Saved as: {file_name}")
    print("\n📱 Scan this QR using any of the apps below to pay:")
    print("⿡ Google Pay")
    print("⿢ PhonePe")
    print("⿣ Other UPI app")

    open_image(file_name)


    print("\n⏳ Waiting for payment confirmation (demo only)...")
    time.sleep(3)
    print("⚠ Reminder: This script can’t auto-check payment.")
    print("Check your UPI app to confirm if amount is credited 💰\n")

def take_order():  #takes order from user
    order_list = []
    total = 0

    # Get customer name for the bill
    customer_name = input("\n👤 Enter customer name: ").strip().title()
    bill_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    while True:
        show_menu()
        try:
            choice = int(input("Enter the item number you want to order: "))
            if choice not in menu:
                print("❌ Invalid choice, try again.")
                continue
            qty = int(input(f"Enter quantity for {menu[choice]['item']}: "))
            if qty <= 0:
                print("⚠ Quantity must be at least 1.")
                continue

            cost = menu[choice]["price"] * qty
            order_list.append((menu[choice]["item"], qty, cost))
            total += cost
        except ValueError:
            print("⚠ Please enter valid numbers only.")
            continue

        more = input("Do you want to add more items? (yes/no): ").lower()
        if more == "no":
            break

    # Print the formatted bill
    print("\n🧾 ----- SANJAY'S RESTAURANT BILL -----")
    print(f"Customer Name : {customer_name}")
    print(f"Date & Time   : {bill_time}")
    print("----------------------------------------")
    for item, qty, cost in order_list:
        print(f"{item:<15} x {qty:<2} = ₹{cost}")
    print("----------------------------------------")
    print(f"Total Amount  = ₹{total}")
    print("----------------------------------------")

    # Use updated UPI ID
    upi_id = "9597121231@fam"
    generate_qr(total, upi_id)
    print("\n💬 Thank you for visiting Sanjay's Restaurant! 😊\n")

def main():    #repeats untill input is no
    while True:
        take_order()
        again = input("Do you want to start a new order? (yes/no): ").lower()
        if again != "yes":
            print("\n👋 Goodbye! Have a nice day!")
            break

if __name__ == "__main__":   #ensures the code runs only when executed directly
    main()
