import sqlalchemy

engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:Makt0112pc-49466@localhost:3306/db_fastapi')


# テーブル名Post
# ユーザー名カラム　固定長10文字 null禁止
# 投稿内容カラム　可変長最大1000文字　空欄OK
engine.execute(
    "CREATE TABLE Post(username CHAR(10) NOT NULL, content VARCHAR(1000) )"
)
