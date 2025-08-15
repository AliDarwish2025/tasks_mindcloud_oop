# البرنامج ده بيشرح الفرق بين النسخ السطحي اللي هو بياخد اكسس على مكان المكان الأصلي في الميموري
# والنسخ العميق اللي بيعمل كوبي بيست للكلام نفسه وبيكون الكلام مستقل، وبالتالي أي تغيير في القائمة
# الأصلية بيأثر في السطحي ولا يؤثر في العميق.

import copy

# مثال النسخ السطحي
print(" Shallow Copy Example ")
data_main = [[6, 2], [3, 4]]
data_clone = copy.copy(data_main)
data_clone[0][0] = 99
print("Original:", data_main)
print("Shallow:", data_clone)

# مثال النسخ العميق
print("\n Deep Copy Example ")
data_main2 = [[6, 2], [3, 4]]
data_full_copy = copy.deepcopy(data_main2)
data_full_copy[0][0] = 42
print("Original:", data_main2)
print("Deep:", data_full_copy)
