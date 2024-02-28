import argparse
import requests
import json
import time

# Function to send message
def send_message(webhook_url, message, count=1):
    for _ in range(count):
        data = {
            "content": message,
            "username": "Webhook Sender"
        }
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print("Message sent successfully.")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
        time.sleep(1)  # Avoid rate limiting


def display_menu():
    print("1. Send a single message")
    print("2. Spam a message")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    return choice

def main():
    parser = argparse.ArgumentParser(description='Send message to Discord via webhook.')
    parser.add_argument("-w", "--webhook", help="Discord webhook URL", required=True)
    args = parser.parse_args()

    while True:
        choice = display_menu()
        if choice == '1':
            message = input("Enter your message: ")
            send_message(args.webhook, message)
        elif choice == '2':
            message = input("Enter your message: ")
            count = int(input("How many times do you want to send the message? "))
            send_message(args.webhook, message, count)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
