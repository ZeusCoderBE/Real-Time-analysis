-- Tạo cơ sở dữ liệu
CREATE DATABASE THEGIOIDIDONG;
GO

-- Sử dụng cơ sở dữ liệu
USE THEGIOIDIDONG;
GO

-- Tạo bảng Device
CREATE TABLE Device (
    id_comment INT IDENTITY PRIMARY KEY,   -- Tự động tăng ID
    product_name NVARCHAR(MAX),            -- Tên sản phẩm
    current_price float ,
    user_name NVARCHAR(MAX),               -- Tên người đánh giá
    user_rating NVARCHAR(MAX),             -- Đánh giá
    user_comment NVARCHAR(MAX),            -- Bình luận của người dùng
    user_time_comment NVARCHAR(MAX)        -- Thời gian sử dụng sản phẩm
);
GO
