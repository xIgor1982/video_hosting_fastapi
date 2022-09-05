import databases
import sqlalchemy

metadata = sqlalchemy.MetaData()
database = databases.Database('sqlite://sqlite.db')
