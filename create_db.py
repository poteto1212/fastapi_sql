import sqlalchemy
engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:Makt0112pc-49466@localhost:3306')

dbname = 'db_fastapi'
engine.execute('CREATE DATABASE %s CHARACTER SET utf8' % dbname)
