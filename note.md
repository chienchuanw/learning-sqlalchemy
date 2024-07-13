# SQLalchemy Learning

## Connect to the database

### Why three slashes?

```python
# connect.py
from sqlalchemy import create_engine

engine = create_engine("sqlite:///sample.db")
```

在使用 SQLAlchemy 連接 SQLite 資料庫時，sqlite:///sample.db 中的三條斜線是有特定含義的：

1. SQLite 資料庫文件路徑：sqlite:///sample.db 表示要連接一個位於相對路徑下的 SQLite 資料庫文件。這裡的三條斜線是為了明確區分出資料庫文件的路徑。

2. 連接字串格式：連接字串的標準格式是 `<database_type>://<username>:<password>@<host>/<database_name>`。對於 SQLite 資料庫來說，不需要使用者名和密碼，也不需要指定主機，所以 `sqlite:///` 後面直接跟資料庫文件的路徑。

相對路徑和絕對路徑：

- `sqlite:///sample.db`：這是相對路徑，表示資料庫文件位於目前工作目錄下。
- `sqlite:////absolute/path/to/sample.db`：這是絕對路徑，注意這裡有四條斜線，第一條斜線是分隔符，後面三條斜線是 UNIX 系統中根目錄的表示。
簡單來說，三條斜線中的前兩條斜線是用來指定相對路徑的格式，第三條斜線則是相對於目前工作目錄的資料庫文件路徑。
