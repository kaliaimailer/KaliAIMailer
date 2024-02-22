import boto3
from botocore.exceptions import ClientError

def send_email_aws_ses(sender, recipient, aws_region, subject, body_text, body_html):
    """Send an email via AWS SES"""
    ses_client = boto3.client('ses', region_name=aws_region)

    try:
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': body_html,
                    },
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': subject,
                },
            },
            Source=sender,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

# Example usage
if __name__ == "__main__":
    sender = "sender@example.com"  # This email must be verified with Amazon SES.
    recipient = "recipient@example.com"
    aws_region = "us-east-1"  # Change to your AWS region
    subject = "Amazon SES Test"
    body_text = ("Amazon SES Test (Python)\r\n"
                 "This email was sent with Amazon SES using the AWS SDK for Python (Boto3).")
    body_html = """<html>
<head></head>
<body>
  <h1>Amazon SES Test (Python)</h1>
  <p>This email was sent with <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the AWS SDK for Python (Boto3).</p>
</body>
</html>
            """

    send_email_aws_ses(sender, recipient, aws_region, subject, body_text, body_html)
