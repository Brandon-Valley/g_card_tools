# l = ['a','b','c','d']
# # 
# # 
# # for e_n, e in enumerate(l):
# # #     print('at top of loop, l: ', l)
# #     print('popping ', e)
# #     
# #     if e == 'd':
# #         l.pop(e_n)
# # 
# #     print('after pop, l: ', l)
# #     
# #     
#     
# for x in l[1:]:
#     print(x)
#     
    
def func2(var):
    return var + ' from func 2'
    
def func1(var1):
    print(func2)
    
func1("hello")