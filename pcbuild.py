import streamlit as st
from streamlit_option_menu import option_menu
import os

# Define the image directory
IMAGE_DIR = "images"

# Sample Product Data (Ensure the image filenames match the ones in the 'images' folder)
products = [
    {"id": 1, "name": "Processor", "price": 27799, "image": "inteli5.jpg"},
    {"id": 2, "name": "Motherboard", "price": 12245, "image": "gigabyte.jpg"},
    {"id": 3, "name": "Graphics Card", "price": 42948, "image": "gpu.jpg"},
    {"id": 4, "name": "SMPS", "price": 5899, "image": "smps.jpg"},
    {"id": 5, "name": "RAM", "price": 10838, "image": "ram.jpg"},
    {"id": 6, "name": "Harddisk", "price": 4299, "image": "hdd.jpg"},
    {"id": 7, "name": "Solid State Drive", "price": 6790, "image": "ssd.jpg"},
    {"id": 8, "name": "Cabinet", "price": 2009, "image": "cabinet.jpg"},
    {"id": 9, "name": "AIO Liquid Cooler", "price": 6589, "image": "liquidcooler.jpg"},
    {"id": 10, "name": "Benq Monitor", "price": 7298, "image": "monitor.jpg"},
]

# Initialize session state for cart if not exists
if "cart" not in st.session_state:
    st.session_state.cart = []

# Function to add item to cart
def add_to_cart(product):
    st.session_state.cart.append(product)
    st.success(f"Added {product['name']} to cart!")

# Function to remove an item from the cart
def remove_from_cart(product_id):
    st.session_state.cart = [item for item in st.session_state.cart if item["id"] != product_id]
    st.rerun()  # Force UI refresh
    

selected_page = option_menu(
    menu_title=None,
    options=["Home", "Cart"],
    icons=['house', 'cart'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    )



# Home Page - Display Products
if selected_page == "Home":
    st.title("🖥 Vetri's Rendering PC for Architects")
    st.write("🛒Browse our configuration and add them to your cart.")

    for product in products:
        col1, col2 = st.columns([1, 3])

        # Get full image path
        image_path = os.path.join(IMAGE_DIR, product["image"])

        with col1:
            st.image(image_path, width=200)  # Display product image
        with col2:
            st.write(f"**{product['name']}**")
            st.write(f"₹ {product['price']:,.2f}")
            if st.button(f"Add {product['name']} to cart", key=product["id"]):
                add_to_cart(product)

# Cart Page - View Added Items
elif selected_page == "Cart":
    st.title("🛒 Your Cart")

    if not st.session_state.cart:
        st.warning("Your cart is empty.")
    else:
        total_price = 0
        for item in st.session_state.cart:
            image_path = os.path.join(IMAGE_DIR, item["image"])
            col1, col2, col3 = st.columns([2, 3, 1])  # Three columns (image, details, remove button)
            with col1:
                st.image(image_path, width=100)  # Display cart item image
            with col2:
                st.write(f"✅ {item['name']} - ₹{item['price']:,.2f}")
            with col3:
                if st.button("❌", key=f"remove_{item['id']}"):
                    remove_from_cart(item["id"])
            total_price += item["price"]
        formatted_total = f"{total_price:,.2f}"  # Format total price
        st.write(f"**Total: ₹{formatted_total}**")
