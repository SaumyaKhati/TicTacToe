class Board:
    def __init__(self, size: int) -> None:
        self.size = size
        self.state = [[0] * size] * size
    pass