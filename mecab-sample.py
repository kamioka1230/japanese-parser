import MeCab
import ipadic

mecab = MeCab.Tagger(ipadic.MECAB_ARGS)
print(mecab.parse('今日は良い天気ですね。'))