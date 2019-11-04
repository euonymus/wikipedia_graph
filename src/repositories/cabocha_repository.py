class CabochaRepository(object):

    def __init__(self):
        import CaboCha
        self.cabocha = CaboCha.Parser()

        
    def parse(self, sentence):
        import CaboCha
        tree = self.cabocha.parse(sentence)
        return tree.toString(CaboCha.CABOCHA_FORMAT_TREE)

