#fio = input().upper()

import pandas as pd
import sqlite3

conn = sqlite3.connect('student.db')
cur = conn.cursor()

file = pd.DataFrame("baza.csv")
'yourtablename'.to_sql("file", conn, if_exists="replace")

conn.commit()





# fio = "БОРИСОВДМИТРИЙДМИТРИЕВИЧ"
# dataset = pd.read_csv('baza.csv', delimiter=',', names=['FIO', 'COURSE1', 'COURSE2'])
# group = pd.read_csv('group.csv', encoding='windows-1251', delimiter=',', names = ['NAME', 'LINK'])

#a = dataset[dataset.FIO == fio]
# print(((str(a.COURSE1)).split())[1])
# print(((str(a.COURSE2)).split())[1])

# a1 = ((str(a.COURSE1)).split())
# a2 = ((str(a.COURSE2)).split())
# print(len(a1))
# print(len(a2))
# a1.remove('Name:')
# a2.remove('Name:')
# a1.remove('COURSE1,')
# a2.remove('COURSE2,')
# a1.remove('dtype:')
# a2.remove('dtype:')
# a1.remove('object')
# a2.remove('object')
#
# a1 = a1[1:]
# a2 = a2[1:]
# print(len(a1))
# print(len(a2))
# print(type(a1))
# print(a1)


# a1 = ((str(a.COURSE1)).split())
# print(a1)
# a2 = ((str(a.COURSE2)).split())
# a1 = a1[1:len(a1)-4]
# a2 = a2[1:len(a2)-4]
#
# s1 = str(a1[0])
# for elem in a1[1:]:
#     s1 = s1 + " " + str(elem)
# print(s1)
#
# s2 = str(a2[0])
# for elem in a2[1:]:
#     s2 = s2 + " " + str(elem)
# print(s2)
#
# b1 = group[group.NAME == str(s1)]
# print((str(b1.LINK)).split()[1])
#
# b2 = group[group.NAME == str(s2)]
# print((str(b2.LINK)).split()[1])


