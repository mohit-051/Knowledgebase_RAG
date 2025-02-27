from internal.interfaces.database_interface import DatabaseInterface
from infastructure.repositories.database_repository import DatabaseRepository


class DatabaseService:

    def __call__(self) -> DatabaseInterface:
        return self

    def __init__(self, database_repository=DatabaseRepository):
        self.database_repository = database_repository

    def insert_one(self, username: str, pdf_name: str, tag: str, description: str):
        data = {
            "pdf_name": pdf_name,
            "tag": tag,
            "username": username,
            "description": description,
        }
        return self.database_repository.insert_one(data, "pdfs")

    def find_all(self, username: str):
        return self.database_repository.find_all("username", username, "pdfs")

    def delete_one(self, username: str, pdf_name: str):
        return self.database_repository.delete_one("pdf_name", pdf_name, "pdfs")

    def check_if_file_belongs_to_user(self, username: str, pdf_name: str):
        return self.database_repository.check_if_file_belongs_to_user(
            username, pdf_name
        )
