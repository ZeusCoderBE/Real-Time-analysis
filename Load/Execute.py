import csv
from Device import Device
from Device_Dao import DeviceDAO

device_dao=DeviceDAO("MSI")
# Đọc dữ liệu từ file CSV
with open('../data/combined_data.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        device = Device(
            product_name=row['Product Name'],
            current_price=float(row['Current Price']),  # Chuyển đổi giá thành float
            user_name=row['Reviewer'],
            user_rating=row['Rating'],
            user_comment=row['Comment'],
            user_time_comment=row['Time Used']
        )
        # Insert vào DB
        device_dao.insert_device(device)
