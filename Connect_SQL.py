import pyodbc
import csv

class PhoneDao:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=GIAHANHUYNH;DATABASE=THEGIOIDIDONG;Trusted_Connection=yes')
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def insert_phone(self, phone_name, phone_price):
        self.cursor.execute("INSERT INTO phone (phone_name, phone_price) VALUES (?, ?)", (phone_name, phone_price))
        self.conn.commit()

    def insert_comment(self, phone_id, user_name, user_rating, user_comment, user_time_comment):
        self.cursor.execute("""
            INSERT INTO comment_phone (id_phone, user_name, user_rating, user_comment, user_time_comment)
            VALUES (?, ?, ?, ?, ?)
        """, (phone_id, user_name, user_rating, user_comment, user_time_comment))
        self.conn.commit()

    def get_phone_id_by_name(self, phone_name):
        self.cursor.execute("SELECT id FROM phone WHERE phone_name = ?", (phone_name,))
        phone_row = self.cursor.fetchone()
        return phone_row[0] if phone_row else None

    def process_csv(self, file_path):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                phone_name, phone_price, user_name, user_rating, user_comment, user_time_comment = row
                phone_id = self.get_phone_id_by_name(phone_name)
                if phone_id is None:
                    self.insert_phone(phone_name, phone_price)
                    phone_id = self.get_phone_id_by_name(phone_name)

                self.insert_comment(phone_id, user_name, user_rating, user_comment, user_time_comment)


if __name__ == '__main__':
    phone_dao = PhoneDao()
    phone_dao.process_csv('./Nhom_2./data/data_Details_Phone_Comment.csv') 
    phone_dao.close()
