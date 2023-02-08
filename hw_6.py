import sqlite3

db = sqlite3.connect("students.db")

b = db.cursor()

b.execute(""" CREATE TABLE IF NOT EXISTS stud(
Name text,
Surname text,
Hobby text,
Mark integer,
Date_of_Birth integer
)
""");

# b.execute("INSERT INTO stud  VALUES('Azret', 'Ajiev', 'history',9,2006)")
# b.execute("INSERT INTO stud  VALUES('Marsel', 'Nazirbaev', 'biology', 10, 2007)")
# b.execute("INSERT INTO stud  VALUES('Bayel', 'Kudayberdiev', 'CS GO', 10, 2006)")
# b.execute("INSERT INTO stud  VALUES('Ali', 'skywhytoxic', 'Faciet', 10, 2007)")
# b.execute("INSERT INTO stud  VALUES('Marat', 'Meyrachov', 'Genshin', 15, 2006)")
# b.execute("INSERT INTO stud  VALUES('Marlen', 'Mamataliev', 'Pubg', 10, 2006)")
# b.execute("INSERT INTO stud  VALUES('Yasin', 'Yunusov', 'volleyball', 11, 2006)")
# b.execute("INSERT INTO stud  VALUES('Bayel', 'Jenishbekov', 'box', 11, 2006)")
# b.execute("INSERT INTO stud  VALUES('Aziret', 'Pirzhanov', 'game', 21, 2006)")
# b.execute("INSERT INTO stud  VALUES('Aman', 'Emilbekov', 'genshin', 11, 2006)")
# b.execute("SELECT rowid, surname FROM stud WHERE LENGTH(surname) >= 10 ")
# print(b.fetchall())
# b.execute("UPDATE stud SET name = 'genius' WHERE mark >= 10")
# b.execute("SELECT rowid, *   FROM stud WHERE name = 'genius'")
# print(b.fetchall())
# b.execute("DELETE FROM stud WHERE rowid % 2 == 0")
db.commit()
db.close()