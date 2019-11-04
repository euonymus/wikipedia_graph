class MecabRepository(object):

    def __init__(self):
        import MeCab
        # self.tagger = MeCab.Tagger("-Ochasen")
        self.tagger = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

    def paragraph_to_list(self, paragraph):
        return paragraph.split('\n')

    def parse_mecabed(self, mecab_morpheme):
        tmp = mecab_morpheme.split('\t')
        if len(tmp) < 2:
            return False
        info = tmp[1].split(',')
        info.insert(0, tmp[0])
        return info

    def morphemize(self, paragraph):
        full_list = list(map(lambda x: self.parse_mecabed(x), self.paragraph_to_list(self.tagger.parse(paragraph))))
        # last 2 items of tagger.parse() are ['EOS', ''], and these should be removed
        return full_list[:-2]

