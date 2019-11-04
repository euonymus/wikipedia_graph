class CabochaRepository(object):

    def __init__(self):
        import CaboCha
        self.cabocha = CaboCha.Parser()

        
    def parse(self, sentence):
        import CaboCha
        print(sentence)
        tree = self.cabocha.parse(sentence)
        print(tree.toString(CaboCha.CABOCHA_FORMAT_TREE))



