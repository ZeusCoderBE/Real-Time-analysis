from Device import Device
import pyodbc

class DeviceDAO:
    def __init__(self, server):
        self.conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE=THEGIOIDIDONG;Trusted_Connection=yes')
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def insert_device(self, device: Device):
        # Thực hiện câu lệnh INSERT vào bảng Device
        self.cursor.execute(
            """
            INSERT INTO Device (product_name, current_price, user_name, user_rating, user_comment, user_time_comment)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (device.product_name, device.current_price, device.user_name, device.user_rating, device.user_comment, device.user_time_comment)
        )
        self.conn.commit()
