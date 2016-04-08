class html_writer():
    def __init__(self, tags_towrite):
        self.tags_towrite = tags_towrite

    def write(self, file):
        with open(file, 'w') as doc:
            for tag in self.tags_towrite:
                firstchar = '<'
