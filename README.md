

Here's a **README.md** file for your GitHub project:

---

# Amazon Price Tracker

This project is a simple **Amazon Price Tracker** that monitors the price of a product on Amazon (or a similar website) and sends an email notification when the price drops below a specified target.

## Features
- Scrapes product prices and titles from the provided URL.
- Sends an email notification when the price is below the set target price.
- Utilizes environment variables for secure storage of sensitive information like email credentials.
- Compatible with Gmail SMTP for email notifications.

---

## Prerequisites
Before running the project, ensure you have the following installed on your system:
- **Python 3.7 or later**
- Required libraries: `requests`, `BeautifulSoup4`, `smtplib`, and `dotenv`

You can install the required Python packages using:
```bash
pip install requests beautifulsoup4 python-dotenv
```

---

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/amazon-price-tracker.git
   cd amazon-price-tracker
   ```

2. Create a `.env` file in the project directory to store sensitive information:
   ```
   my_email=your_email@example.com
   password=your_app_password
   ```

   Replace `your_email@example.com` with your email and `your_app_password` with your Gmail app password. Learn more about generating an app password [here](https://support.google.com/accounts/answer/185833?hl=en).

3. Update the **target price** and **URL** in the script:
   ```python
   TARGET_PRICE = 100.00  # Replace with your desired target price
   URL = "https://example.com/product"  # Replace with the product URL
   ```

---

## Running the Script

Run the script using the following command:
```bash
python price_tracker.py
```

If the product price is below the target price, an email will be sent to the configured email address.

---

## How It Works

1. The script fetches the HTML content of the product page using the `requests` library.
2. It parses the HTML using `BeautifulSoup` to extract the product price and title.
3. If the extracted price is below the target price, the script sends an email notification via Gmail's SMTP server.

---

## Important Notes

1. **Using a Public Website:** The example URL (`https://appbrewery.github.io/instant_pot/`) is a public website, not Amazon. If you're using an Amazon URL, ensure compliance with Amazon's terms of service.
2. **Gmail SMTP Restrictions:** Make sure to enable "Allow less secure apps" or generate an app password for your Gmail account to avoid login issues.
3. **Dynamic Content:** If the product page content is dynamically loaded (e.g., via JavaScript), this script may not work as expected. Consider using tools like `selenium` for such cases.

---

## Future Enhancements
- Add support for multiple product URLs.
- Implement a scheduler to run the script at regular intervals.
- Integrate with more email providers (e.g., Outlook, Yahoo).
- Enhance error handling for dynamic or unavailable content.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

--- 

Feel free to customize it further based on your needs! Let me know if you'd like to adjust any section.
