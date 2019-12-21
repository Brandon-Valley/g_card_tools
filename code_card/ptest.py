# 
# import file_system_utils as fsu
# 
# dir_path = "F:\\Calendars (2019)\\Calendars (2019) JPG"
# 
# 
# 
# img_path_l = fsu.get_dir_content_l(dir_path, 'file', 'abs_path')
# print(len(img_path_l))
# 
# # 
# # for img_path in img_path_l:
# #     bn = fsu.get_basename_from_path(img_path)
# #     if '-' in bn and '-0' not in bn:
# #         fsu.delete_if_exists(img_path)


from datetime import date
from datetime import datetime


# print(date.today())
# print(datetime.now())
# 
# t = datetime(2012, 3, 5, 23, 8, 15)
# print(t)
# dts = str(datetime.now())
# print(dts)
# s=  str(datetime.date() + ' ' + datetime.time())
# print(s)



mydate = datetime.now()
csvstr = datetime.strftime(mydate, '%Y, %m, %d, %H, %M, %S')
# dt = datetime(csvstr, '%Y, %m, %d, %H, %M, %S')
# print(dt)
print(csvstr)

