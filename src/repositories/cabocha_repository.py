class CabochaRepository(object):

    def __init__(self):
        import CaboCha
        self.cabocha = CaboCha.Parser("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
        
    def parse(self, sentence):
        import CaboCha
        tree = self.cabocha.parse(sentence)

        chunkId = 0
        for i in range(0, tree.size()):
            token = tree.token(i)
            if token.chunk != None:
                print(chunkId, token.chunk.link, token.chunk.head_pos, 
                      token.chunk.func_pos, token.chunk.score)
                chunkId += 1

            print('========================')
            print(token.surface, token.feature, token.ne)
            print('-----------------------')


        tree_format =  tree.toString(CaboCha.FORMAT_TREE)
        lattice_format = tree.toString(CaboCha.FORMAT_LATTICE)
        print(tree_format)
        print(lattice_format)
        return tree_format
