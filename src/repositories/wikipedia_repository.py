class WikipediaRepository(object):

    def __init__(self):
        None
        # import MeCab
        # self.tagger = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

    def read_text(self, title):
        import urllib
        import requests
        from bs4 import BeautifulSoup

        encoded_title = urllib.parse.quote(title)
        wikipedia_url = requests.get('https://ja.wikipedia.org/wiki/%s' % (encoded_title))

        # Get Html
        soup = BeautifulSoup(wikipedia_url.content, 'lxml')

        # Remove script and style attributes
        for script in soup(["script", "style"]):
            script.decompose()

        #print(soup.prettify)
        # Get only Text
        raw_text = soup.get_text()

        # Put lines in a list
        all_lines= [line.strip() for line in raw_text.splitlines()]

        # Make the list into text without empty lines
        all_text="\n".join(line for line in all_lines if line)

        return all_text
