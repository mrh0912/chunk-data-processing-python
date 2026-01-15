# Project 0.1 – CSV Ingestion & Data Cleaning (Python)

## 📌 Mục tiêu
Project này nhằm luyện tập các kỹ năng nền tảng của Data Engineering:
- Đọc dữ liệu CSV dung lượng lớn bằng chunk
- Làm sạch dữ liệu (missing values, duplicate, type casting)
- Tổ chức code theo cấu trúc project chuẩn
- Chuẩn bị cho các pipeline ETL sau này

---

## 📂 Cấu trúc thư mục

roject_0.1/
│
├── scripts/
│ ├── ingest.py # Đọc dữ liệu CSV bằng chunksize
│ ├── clean.py # Làm sạch dữ liệu
│ └── config.py # Cấu hình đường dẫn & tham số
│
├── data/
│ ├── raw/ # Dữ liệu gốc (KHÔNG push Git)
│ └── clean/ # Dữ liệu đã làm sạch
│
├── .gitignore
├── requirements.txt
└── README.md

---

## 📊 Dataset
Dataset sử dụng: **Sales / E-commerce dataset**

Nguồn: Kaggle  
(Link dataset được cung cấp riêng, không lưu dữ liệu vào repo)

Sau khi tải dataset:
- Đặt file CSV vào: data/raw/

---

## ⚙️ Cài đặt môi trường

```bash
pip install pandas
python scripts/ingest.py
python scripts/clean.py

