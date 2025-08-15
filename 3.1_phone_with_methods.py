# الكود ده عن مميزات الموبايل الأساسية اللي ليها علاقة بالأسماء والمكالمات
# فيه لستة نخزن فيها الأسماء، ونقدر نضيف، نمسح، أو نكلم اي حد من خلالها

class Phone:
    def __init__(self):
        self.contacts = []  

    def add_cont(self, name): 
        if name not in self.contacts:
            self.contacts.append(name)
            print(f"تمت إضافة {name} في الأسماء.")
        else:
            print("الاسم اتسجل قبل كده.")

    def remove_contact(self, name): 
        if name in self.contacts:
            self.contacts.remove(name)  
            print(f"تم حذف {name} من الأسماء.")
        else:
            print("الاسم مش موجود.")

    def call(self, name):  
        if name in self.contacts:
            print(f"calling {name}...")
        else:
            print("الاسم مش موجود في الأسماء.")



mob = Phone()

mob.add_cont("أحمد")
mob.add_cont("سارة")
mob.add_cont("أحمد")   

mob.call("أحمد")
mob.call("محمد")       

mob.remove_contact("سارة")
mob.remove_contact("محمود")  
