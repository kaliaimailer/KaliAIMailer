# report_to_admin.py

from reporting.reporting_to_admin import send_email

def main():
    subject = "Daily Operations Report"
    body = "Here is the daily report of operations..."
    send_email(subject, body)

if __name__ == "__main__":
    main()
