class MecabRepository(object):

    def __init__(self):
        import MeCab
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

    def retrieve_proper_nouns(self, paragraph):
        from constants.labels import labels
        morphemes = self.morphemize(paragraph)

        proper_nouns = []
        for morpheme in morphemes:
            if not morpheme or morpheme[2] != '固有名詞':
                continue

            if morpheme[3] == '人名':
                if morpheme[4] != '一般':
                    continue
                label = labels['LABEL_PERSON']
            elif morpheme[3] == '組織':
                label = labels['LABEL_ORGANIZATION']
            elif morpheme[3] == '地域':
                if morpheme[4] == '国':
                    label = labels['LABEL_COUNTRY']
                else:
                    label = labels['LABEL_AREA']
            else:
                label = labels['LABEL_THING']

            proper_nouns.append({'name': morpheme[0], 'label': label})

        return proper_nouns
