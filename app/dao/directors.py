from typing import Dict, Any


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        pass

    def get_one(self, uid: int):
        pass

    def update(self, uid: int, data: Dict[str, Any]):
        pass

    def create(self, data: Dict[str, Any]):
        pass

    def delete(self, uid: int):
        pass