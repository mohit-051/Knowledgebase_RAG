from flask import Flask, request, jsonify
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
        self.expiration_time = int(os.getenv("EXPIRATION_TIME", 60))

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


# Initialize Flask app
app = Flask(__name__)
aws_repo = AWSRepository()


@app.route("/upload_pdf", methods=["POST"])
def upload_pdf():
    file = request.files["file"]
    if file and file.filename.endswith(".pdf"):
        file_content = file.read()
        if aws_repo.upload_pdf(file.filename, file_content):
            return jsonify({"message": "File uploaded successfully"}), 200
        else:
            return jsonify({"message": "Failed to upload file"}), 500
    else:
        return jsonify({"message": "Invalid file type"}), 400


@app.route("/get_presigned_pdf_url/<file_name>", methods=["GET"])
def get_presigned_pdf_url(file_name):
    url = aws_repo.get_presigned_pdf_url(file_name)
    if url:
        return jsonify({"url": url}), 200
    else:
        return jsonify({"message": "Failed to generate presigned URL"}), 500


if __name__ == "__main__":
    app.run(debug=True)
