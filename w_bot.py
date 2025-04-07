import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def send_whatsapp_message(contact_name, message_text):
    try:
        # Locate the search box and enter contact name
        search_box = browser.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.clear()
        search_box.send_keys(contact_name)
        time.sleep(2)

        # Click on the contact name
        contact = browser.find_element(By.XPATH, f'//span[@title="{contact_name}"]')
        contact.click()
        time.sleep(2)

        # Type the message
        message_box = browser.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.click()
        message_box.send_keys(message_text)
        time.sleep(1)

        # Click the send button
        send_button = browser.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_button.click()

        print(f"✅ Message sent to {contact_name}")
    except Exception as e:
        print(f"❌ Failed to send message to {contact_name}: {e}")

# --- Main script starts here ---

# Configure ChromeDriver
chrome_options = webdriver.ChromeOptions()
service = Service('chromedriver.exe')
browser = webdriver.Chrome(service=service, options=chrome_options)

# Open WhatsApp Web
browser.get("https://web.whatsapp.com")
print("📱 Please scan the QR code in the browser window to log into WhatsApp.")
time.sleep(20)  # Time to scan QR

# List of contacts and message
contacts = ['Kiruba']  #  Make sure this name matches WhatsApp contact name exactly
message = "Hi! This is an automated message sent using Selenium."

# Send message to each contact
for name in contacts:
    send_whatsapp_message(name, message)

# Keep the browser open for a while before closing
print("✅ All messages sent. Browser will close in 15 seconds.")
time.sleep(15)
browser.quit()
