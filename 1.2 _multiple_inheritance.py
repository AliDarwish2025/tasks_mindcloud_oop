# الكود ده بيوضح يعني إيه "ميراث متعدد" في بايثون
# يعني الإبن ممكن ياخد صفات ودوال من أكتر من أب في نفس الوقت
# لو الإبن والأب عندهم نفس الدالة، الإبن بيغطي على الأب (الأولوية للأحدث اللي مكتوب)
# ولو فيه أبين ليهم نفس الجد (اللي بنسميه مشكلة الـ Diamond)، بايثون بيحلها بترتيب الـ MRO
# يعني بيبص على ترتيب الوراثة اللي إنت كاتبه في الكود ويمشي عليه أول ما يلاقي الدالة ينفذها

#   1: ميراث متعدد عادي 
class Father:
    def work(self):
        print(" الأب بيشتغل مهندس")

class Mother:
    def cook(self):
        print(" الأم بتطبخ ")

class Child(Father, Mother):
    pass

print(" الميراث المتعدد ")
c = Child()
c.work()
c.cook()

# 2: نفس الدالة موجودة عند الأب والإبن 
class Parent:
    def speak(self):
        print("الأب = صباح الخير")

class Son(Parent):
    def speak(self):
        print(" الإبن = صباح النور")

print("\n نفس الميثود في الأب والإبن  ")
s = Son()
s.speak()  # هتنفذ بتاعة الإبن لأنه غطى على الأب

# مثال 3: الاتنين آباء ليهم نفس الجد (مشكلة الـ Diamond) 
class Grandparent:
    def greet(self):
        print(" الجد =  هلاً")

class Dad(Grandparent):
    def greet(self):
        print(" الأب = أهلاً وسهلاً")

class Mum(Grandparent):
    def greet(self):
        print(" الأم  = مرحباً")

class Kid(Dad, Mum):
    pass

print("\n  Diamond Problem ")
k = Kid()
k.greet()  # بايثون هنا هينفذ دالة الأب عشان ترتيب الوراثة Kid(Dad, Mum)
print(Kid.__mro__) #الترتيب اللي بيدور فيه البايثون علي ال methods و الصفات .
