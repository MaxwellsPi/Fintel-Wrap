import pandas as pd
from sqlalchemy import create_engine
import os


class SQLDB:
    def __init__(self, source: str = 'fintel'):
        self.source = source
        self.dir = os.path.join(os.getcwd(), 'data', 'db')
        self.path = os.path.join(self.dir, f"{source}.db")
        self.engine = create_engine(r'sqlite:///{}'.format(self.path), echo=False)

        os.makedirs(self.dir, exist_ok=True)

    def load_sql(self, df: pd.DataFrame, table_name: str = 'test'):
        print(f'Loading data to {table_name} in {self.source}.db')
        df.to_sql(table_name, con=self.engine, if_exists='append', index=False)

    def disconnect(self):
        self.engine.dispose()


