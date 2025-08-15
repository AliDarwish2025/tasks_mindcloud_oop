# الكود ده بيعمل نظام تصويت بسيط باستخدام الـ OOP في بايثون
# فيه 4 وظائف أساسية: تضيف مرشح، تحذف مرشح، تصوت لمرشح، وتعرض الفائز
# عاملين الـ بيانات private (مقفولة) عشان محدش يقدر يلعب فيها من برة الكلاس (Encapsulation)

class VotingSystem:
    def __init__(self):
        self.__candidates = {}

    def add_cand(self, name):  
        if name not in self.__candidates:
            self.__candidates[name] = 0
            print(f"تم إضافة المرشح: {name}")
        else:
            print("المرشح موجود .")

    def rem_cand(self, name): 
        if name in self.__candidates:
            del self.__candidates[name]
            print(f"تم حذف المرشح: {name}")
        else:
            print("المرشح غير موجود.")

    def vote_to_candidate(self, name):
        if name in self.__candidates:
            self.__candidates[name] += 1
            print(f"تم التصويت لـ {name}")
        else:
            print("المرشح غير موجود.")

    def winner(self):
        if not self.__candidates:
            print("لا يوجد مرشحين.")
            return
        winner = max(self.__candidates, key=self.__candidates.get)
        print(f"الفائز هو: {winner} بعدد أصوات {self.__candidates[winner]}")

voting = VotingSystem()
voting.add_cand("أحمد")
voting.add_cand("سارة")
voting.add_cand("محمد")
voting.add_cand("سارة")

voting.vote_to_candidate("أحمد")
voting.vote_to_candidate("محمد")
voting.vote_to_candidate("أحمد")

voting.winner()
