import MeCab

mecab = MeCab.Tagger('-Ochasen')
print(mecab.parse('今日は良い天気ですね。'))