from dataclasses import dataclass

@dataclass
class Color:
    red: int
    green: int
    blue: int

    def __post_init__(self):
        assert self.red >= 0 and self.red <= 255
        assert self.green >= 0 and self.green <= 255
        assert self.blue >= 0 and self.blue <= 255

    def rgb(self) -> tuple:
        return (self.red,self.green,self.blue,)

    

