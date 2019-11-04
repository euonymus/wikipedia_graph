import pytest
from libs.text_utils import TextUtils

class TestTextUtils(object):

    @pytest.mark.parametrize("text, expected", [
        ("明仁（あきひと、（1933年〈昭和8年〉12月23日 - ））は、日本の第125代天皇（在位:1989年〈昭和64年〉1月7日 - 2019年〈平成31年〉4月30日）[注釈 2]、上皇（在位:2019年〈令和元年〉5月1日 - ）。称号は繼宮（つぐのみや）[4]、お印は榮（えい）[5]。敬称は陛下[6]。勲等は大勲位菊花章頸飾。", "明仁は、日本の第125代天皇、上皇。称号は繼宮、お印は榮。敬称は陛下。勲等は大勲位菊花章頸飾。"),
    ])
    def test_nodes_in_paragraph(self, text, expected):
        text_utils = TextUtils()
        result = text_utils.delete_brackets(text)
        assert result == expected




