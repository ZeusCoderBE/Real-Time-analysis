-- Tạo bảng phone
CREATE TABLE phone (
    id INT IDENTITY PRIMARY KEY,
    phone_name NVARCHAR(MAX),
    phone_price NVARCHAR(MAX),
);
GO

-- Tạo bảng comment
CREATE TABLE comment_phone (
	id_comment INT IDENTITY PRIMARY KEY,
    id_phone INT,
    user_name NVARCHAR(MAX),
	user_rating NVARCHAR(MAX),
    user_comment NVARCHAR(MAX),
	user_time_comment NVARCHAR(MAX)
    FOREIGN KEY (id_phone) REFERENCES phone(id),
);