import pandas as pd
from config import RAW_DATA_PATH, CLEAN_DATA_PATH, CHUNK_SIZE

def clean_chunk(df):
    # 1. Drop missing giá trị quan trọng
    df = df.dropna(subset=["InvoiceNo", "InvoiceDate", "CustomerID"])

    # 2. Chuẩn hóa kiểu dữ liệu
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")

    df = df.dropna(subset=["InvoiceDate", "Quantity", "UnitPrice"])

    # 3. Lọc dữ liệu sai
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]

    # 4. Remove duplicates
    df = df.drop_duplicates(subset=["InvoiceNo", "StockCode"])

    return df

def process():
    first_chunk = True

    for chunk in pd.read_csv(RAW_DATA_PATH, chunksize=CHUNK_SIZE):
        cleaned = clean_chunk(chunk)

        cleaned.to_csv(
            CLEAN_DATA_PATH,
            mode="w" if first_chunk else "a",
            header=first_chunk,
            index=False
        )

        print(f"Written {len(cleaned)} rows")
        first_chunk = False

if __name__ == "__main__":
    process()
