import sqlite3
conn = sqlite3.connect("survey.sqlite")
cursor = conn.cursor()
result = cursor.execute("SELECT * FROM students WHERE selfstudyhour > 2")
for row in result:
    print(row)
def fnction(instagram,age):
    result = ("SELECT count(id) as count_fromstudents FROM students ")
    print(result)
    cursor.execute(""" INSERT INTO students (ID,Age,OnlineClassTime,Devise,SelfStudyHour,FitnessTime,Sleep,SocialMedia,SocialMediaPlatform) VALUES(498,28,7,'smartphone',8,4,8,3,instagram)""")
    conn.commit()
result = cursor.execute("UPDATE students SET Devise ='anamaraia',  WHERE age > 19")
conn.commit()

conn.close()

#davaleba2
import requests
import json

with open('sample.json') as json_file:
    r = json.load(json_file)
    print(r)
    person = r.get('person')
    eyecolor = r.get("eyecolor")
    print('color')
    friends = r['person']['friends']
for friends in person['friends']:
    print(person[''])







