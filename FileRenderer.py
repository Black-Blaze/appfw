class FileRenderer:
    def __init__(self):
        pass

    def render(self, file):
        with open(file) as f:
            return f.read()