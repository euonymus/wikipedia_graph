import pytest
from repositories.mecab_repository import MecabRepository

class TestMecabRepository(object):

    @pytest.mark.parametrize("text, expected", [
        ("尊敬しているフィギュアスケート選手は伊藤みどり、エフゲニー・プルシェンコ。伊藤の衣装を着用して競技に臨んだこともあり、「みどりさんの衣装を着るといつも調子がいい」と語っていた\n長野オリンピック金メダリストのタラ・リピンスキーにも憧れの言葉を寄せており、彼女の演技を見て自分もオリンピックに出たいと思うようになったという。", ['尊敬しているフィギュアスケート選手は伊藤みどり、エフゲニー・プルシェンコ。伊藤の衣装を着用して競技に臨んだこともあり、「みどりさんの衣装を着るといつも調子がいい」と語っていた','長野オリンピック金メダリストのタラ・リピンスキーにも憧れの言葉を寄せており、彼女の演技を見て自分もオリンピックに出たいと思うようになったという。']),
    ])
    def test_paragraph_to_list(self, text, expected):
        mecab = MecabRepository()
        result = mecab.paragraph_to_list(text)
        assert result == expected

    @pytest.mark.parametrize("text, expected", [
        ('浅田真央\t名詞,固有名詞,人名,一般,*,*,浅田真央,アサダマオ,アサダマオ', ['浅田真央', '名詞', '固有名詞', '人名', '一般', '*', '*', '浅田真央', 'アサダマオ', 'アサダマオ']),
    ])
    def test_parse_mecabed(self, text, expected):
        mecab = MecabRepository()
        result = mecab.parse_mecabed(text)
        assert result == expected

    @pytest.mark.parametrize("text, expected", [
        ("浅田真央は名古屋出身のフィギュアスケーター", [['浅田真央', '名詞', '固有名詞', '人名', '一般', '*', '*', '浅田真央', 'アサダマオ', 'アサダマオ'], ['は', '助詞', '係助詞', '*', '*', '*', '*', 'は', 'ハ', 'ワ'], ['名古屋出身', '名詞', '固有名詞', '一般', '*', '*', '*', '名古屋出身', 'ナゴヤシュッシン', 'ナゴヤシュッシン'], ['の', '助詞', '連体化', '*', '*', '*', '*', 'の', 'ノ', 'ノ'], ['フィギュアスケーター', '名詞', '固有名詞', '一般', '*', '*', '*', 'フィギュアスケーター', 'フィギュアスケーター', 'フィギュアスケーター']]),
    ])
    def test_morphemize(self, text, expected):
        mecab = MecabRepository()
        result = mecab.morphemize(text)
        assert result == expected

