import sqlalchemy
from sqlalchemy.sql.functions import user
engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:Makt0112pc-49466@localhost:3306/db_fastapi')

samplelist = [
    {'username': 'ユーザー1', 'content':  'ユーザー１の投稿'},
    {'username': 'Test2', 'content':  'Test2spost'},
    {'username': 'Test3', 'content':  'Test3spost'},
]

for sample in samplelist:
    username = sample['username']
    content = sample['content']
    engine.execute(
        f"INSERT INTO Post (username,content) VALUES ('{username}','{content}')")
