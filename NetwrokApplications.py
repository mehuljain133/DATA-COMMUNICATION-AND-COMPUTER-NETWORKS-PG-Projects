# Unit-VII Network Applications: File transfer protocol, electronic mail, World Wide Web.

import time
import random

# Constants for simulation
MAX_FILE_SIZE = 50  # Maximum file size in MB for FTP
MAX_EMAIL_SIZE = 5  # Maximum email size in MB
MAX_WEBSITE_SIZE = 20  # Max website page size in MB

# Simulating FTP (File Transfer Protocol)
def ftp_transfer(file_name):
    print("\n--- FTP (File Transfer Protocol) Simulation ---")
    
    # Simulating file transfer with a random file size (between 1 MB and MAX_FILE_SIZE MB)
    file_size = random.randint(1, MAX_FILE_SIZE)
    print(f"Initiating file transfer: {file_name} (Size: {file_size} MB)")
    
    # Simulate the file transfer process
    transfer_time = file_size / 10  # Assume transfer speed is 10 MB/sec
    time.sleep(transfer_time)
    
    print(f"File transfer complete: {file_name} (Size: {file_size} MB)")

# Simulating Email (Electronic Mail)
def send_email(sender, receiver, subject, message):
    print("\n--- Electronic Mail (Email) Simulation ---")
    
    # Simulating the size of the email message (between 1 MB and MAX_EMAIL_SIZE MB)
    email_size = random.randint(1, MAX_EMAIL_SIZE)
    
    print(f"From: {sender}")
    print(f"To: {receiver}")
    print(f"Subject: {subject}")
    print(f"Message: {message[:50]}...")  # Show only the first 50 characters of the message
    print(f"Email size: {email_size} MB")
    
    # Simulate email sending process (it could take a few seconds)
    time.sleep(2)
    
    print(f"Email sent successfully to {receiver}. Size: {email_size} MB")

# Simulating World Wide Web (WWW)
def visit_website(url):
    print("\n--- World Wide Web (WWW) Simulation ---")
    
    # Simulate accessing a website with a random page size (between 1 MB and MAX_WEBSITE_SIZE MB)
    page_size = random.randint(1, MAX_WEBSITE_SIZE)
    print(f"Accessing website: {url} (Page size: {page_size} MB)")
    
    # Simulate the time it takes to load the page (assume it takes 1 second per MB)
    load_time = page_size
    time.sleep(load_time)
    
    print(f"Website loaded successfully: {url}. (Page size: {page_size} MB)")

# Main function to simulate network applications
def main():
    # Simulate FTP File Transfer
    ftp_transfer("example_file.txt")
    
    # Simulate sending an Email
    send_email(
        sender="alice@example.com",
        receiver="bob@example.com",
        subject="Meeting Schedule",
        message="Hi Bob, I wanted to confirm our meeting schedule for next week. Please let me know your availability."
    )
    
    # Simulate visiting a website
    visit_website("https://www.example.com")

if __name__ == "__main__":
    main()
