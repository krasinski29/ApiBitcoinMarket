import os
import datetime
from typing import List
import json

class DataTypeNotSupportedForIngestionException(Exception):

    def __init__(self,data):
        self.data = data
        self.message =f"Data type {type(data)} is not supported for ingestion"
        super().__init__(self.message)

class DataWriter():

    def __init__(self, coin: str, api: str) -> None:
        self.api = api
        self.coin = coin
        self.filename = f"{self.api}/{self.coin}/{datetime.date.today()}_{datetime.datetime.now().time().strftime('%Hh%Mm%Ss')}.json"

    def _write_row(self, row: str) -> None:
        os.makedirs(os.path.dirname(self.filename),exist_ok=True)
        with open(self.filename,"a") as f:
            f.write(row)

    def write(self, data: {List, dict}):
        if isinstance(data, dict):
            self._write_row(json.dumps(data) + "\n")
        elif isinstance(data,List):
           for element in data:
                self.write(element)
        else:
            raise DataTypeNotSupportedForIngestionException(data)
