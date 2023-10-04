class MarkdownWritter:
    cariage_return:str
    data:str = ""

    def __init__(self, carriage_return = "\n\n") -> None:
        self.cariage_return = carriage_return

    def log(self, content):
        self.data += f"{content}{self.cariage_return}"

    def dump(self):
        return self.data
    
    def dump_in_file(self, path):
        with open(path, mode="w") as file:
            file.write(self.dump())

    @staticmethod
    def img(image_url, alt="todo"):
        return f'<img src="{image_url}" alt="{alt}" width="20px" height="20px">'