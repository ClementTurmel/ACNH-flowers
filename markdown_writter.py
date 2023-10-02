class MarkdownWritter:
    data:str = ""

    def log(self, content):
        self.data += f"{content}\n"

    def dump(self):
        return self.data
    
    def dump_in_file(self, path):
        with open(path, mode="w") as file:
            file.write(self.dump())

    @staticmethod
    def img(image_url, alt="todo"):
        return f'<img src="{image_url}" alt="{alt}" width="20px" height="20px">'