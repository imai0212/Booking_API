from sqlalchemy import Column, ForeignKey, Integer, String , DateTime
from .database import Base


# DB側のデータ構造
class User(Base):
    # Baseの継承により以下形式でテーブル設定可
    __tablename__ = 'users'
    # 主キー指定によってuser_idでの判別優先, 検索を早くするためのindex
    user_id = Column(Integer, primary_key=True, index=True)
    # unique=True：他ユーザーとの被りを許可しない
    username = Column(String, unique=True, index=True)

class Room(Base):
    __tablename__ = 'rooms'
    room_id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String, unique=True, index=True)
    capacity = Column(Integer)

class Booking(Base):
    __tablename__ = 'bookings'
    booking_id = Column(Integer, primary_key=True, index=True)
    # 外部キーとの連携、親が削除されると連動して消す、未入力不可
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='SET NULL'), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.room_id', ondelete='SET NULL'), nullable=False)
    booked_num = Column(Integer)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)
