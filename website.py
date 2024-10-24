import streamlit as st

# Sample menu items
menu = {
    "Pizza": 12.99,
    "Burger": 8.99,
    "Sushi": 15.99,
    "Pasta": 10.99,
    "Salad": 7.99
}

# Function to display the menu
def show_menu():
    st.title("Online Food Ordering")
    st.header("Menu")
    for item, price in menu.items():
        st.write(f"{item}: ${price:.2f}")

# Function to take orders
def take_order():
    st.header("Place Your Order")
    order = {}
    for item in menu.keys():
        quantity = st.number_input(f"How many {item}?", min_value=0, value=0)
        if quantity > 0:
            order[item] = quantity
    
    if st.button("Submit Order"):
        if order:
            st.success("Order placed successfully!")
            total_price = sum(menu[item] * qty for item, qty in order.items())
            st.write("Your Order:")
            for item, qty in order.items():
                st.write(f"{item}: {qty}")
            st.write(f"Total Price: ${total_price:.2f}")
        else:
            st.warning("Please select at least one item.")

# Main function to run the app
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Menu", "Order"])
    
    if selection == "Menu":
        show_menu()
    elif selection == "Order":
        take_order()

if __name__ == "__main__":
    main()
