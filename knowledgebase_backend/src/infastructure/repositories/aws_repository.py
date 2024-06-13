import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class AWSRepository:

    def __init__(self):
        # Initialize the AWSRepository class with the required configuration
        self.aws_bucket_name = os.getenv("AWS_BUCKET_NAME")
        self.aws_access_key = os.getenv("AWS_ACCESS_KEY")
        self.aws_secret_key = os.getenv("AWS_SECRET_KEY")
        self.aws_service = "s3"
        self.s3_client = boto3.client(
            self.aws_service,
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_key,
        )
        self.expiration_time = 60

    def upload_pdf(self, file_name, file_content):
        try:
            # Upload the file to the S3 bucket
            self.s3_client.put_object(
                Bucket=self.aws_bucket_name, Key=file_name, Body=file_content
            )
            return True
        except Exception as e:
            print(f"Error uploading {file_name} to S3: {e}")
            return False

    def get_presigned_pdf_url(self, file_name):
        try:
            # Generate a presigned URL for the file
            url = self.s3_client.generate_presigned_url(
                ClientMethod="get_object",
                Params={
                    "Bucket": self.aws_bucket_name,
                    "Key": file_name,
                    "ResponseContentDisposition": "inline",
                    "ResponseContentType": "application/pdf",
                },
                ExpiresIn=self.expiration_time,
            )
            print(f"Generated URL for {file_name}: {url}")
            return url
        except Exception as e:
            print(f"Error generating presigned URL for {file_name}: {e}")
            return None


# Example usage:
if __name__ == "__main__":
    aws_repo = AWSRepository()
    aws_repo.upload_pdf("example.pdf", b"sample pdf content")
    aws_repo.get_presigned_pdf_url("example.pdf")
