import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv(dotenv_path=r"C:\Users\sanid\OneDrive\Desktop\python 2 udemy\day47\.env")

# Fetch email and app password directly from environment variables
CLIENT_EMAIL = os.environ['my_email']  # Accessing the email from environment
CLIENT_PASSWORD = os.environ['password']  # Accessing the app password

# Set the target price you want to track
TARGET_PRICE = 100.00

# Amazon product URL (replace with actual URL)
URL = "https://appbrewery.github.io/instant_pot/"  # Example URL

# Send a GET request to the Amazon product page
response = requests.get(URL)
response.raise_for_status()

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find the price on the page (using the correct CSS class)
price_tag = soup.find(class_="a-offscreen")
if price_tag:
    price = price_tag.get_text()
    price_no_dollar = price.split("$")[1]  # Split and remove the dollar sign
    price_as_float = float(price_no_dollar)

    # Extract product title
    product_title = soup.find(id="productTitle")
    if product_title:
        product_title = product_title.getText().strip()

    # Check if the price is below the target price
    if price_as_float < TARGET_PRICE:
        # Prepare email message
        message = f"Subject: Amazon Price Alert\n\n{product_title}\n{URL}\nPrice: ${price_as_float}"

        # Send email notification
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=CLIENT_EMAIL, password=CLIENT_PASSWORD)
            
            # Encode the message to UTF-8 to avoid UnicodeEncodeError
            message = message.encode('utf-8')
            connection.sendmail(from_addr=CLIENT_EMAIL, to_addrs=CLIENT_EMAIL, msg=message)
            print(f"Email sent for {product_title} at ${price_as_float}")
    else:
        print(f"Price of {product_title} is above the target price. Current price: ${price_as_float}")
else:
    print("Could not find the price on the page.")
