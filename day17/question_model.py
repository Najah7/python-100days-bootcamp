# NOTE:動画ではQuestionをクラスにしていた（辞書型→オブジェクトに）
#   個人的にattrが2つでメソッドはないので、辞書型のままの方がいいと思い、オブジェクト化せず。quizクラスを実装


class Question:
    
    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer