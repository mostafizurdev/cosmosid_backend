import databases
import sqlalchemy

DATABASE_URL = "postgresql://mostafizurdev:admin1234@db/cosmosid_db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

taxonomy_data = sqlalchemy.Table(
    "taxonomy_data",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("taxonomy_level", sqlalchemy.String),
    sqlalchemy.Column("result_data", sqlalchemy.Text)
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
