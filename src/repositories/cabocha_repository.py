class CabochaRepository(object):

    def __init__(self):
        import CaboCha
        self.cabocha = CaboCha.Parser("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
        
    def parse(self, sentence):
        import CaboCha
        tree = self.cabocha.parse(sentence)
        tree_format =  tree.toString(CaboCha.FORMAT_TREE)
        lattice_format = tree.toString(CaboCha.FORMAT_LATTICE)
        print(tree_format)
        print(lattice_format)
        return tree_format
