from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 同じディレクトリ内にDB格納用ファイルを作成
SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
# CRUDなどの操作を行うための基盤作成（check_same_thread：SQLite専用引数）
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
# DBへの接続から切断までの流れを定義
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# DB構造作成用のクラス
Base = declarative_base()
