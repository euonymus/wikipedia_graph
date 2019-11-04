class Graph(object):

    def __init__(self):
        from repositories.mecab_repository import MecabRepository
        self.mecab = MecabRepository()

    def nodes_in_paragraph(self, paragraph):
        from constants.labels import labels
        morphemes = self.mecab.morphemize(paragraph)

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

