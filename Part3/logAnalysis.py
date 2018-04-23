#! /usr/bin/env

import psycopg2
import time

DBNAME = "news"

#Questions and Answers that we want the answers to!
#Answers refer here to the queries
question1 = """
Which are the most popular three articles of all time?
"""
answer1 = """
SELECT title, num FROM top_articles LIMIT 3;
"""


question2 = """
Who are the most popular article authors of all time?
"""
answer2 = """
SELECT * FROM top_authors;
"""


question3 = """
On which days did more than 1% of requests lead to errors?
"""
answer3 = """
SELECT * FROM error_percentage WHERE error_rate > 1.0;
"""

def answers():
    #connect to the database
    db = psycopg2.connect(database=DBNAME)
    #cursor object
    cursor = db.cursor()

    #Fetching most popular articles
    cursor.execute(answer1)
    results = cursor.fetchall()
    print(question1)
    for result in results:
        print('{} -- {}'.format(result[0], result[1]))
    print('\n\n')

    #Fetching most popular authors
    cursor.execute(answer2)
    results = cursor.fetchall()
    print(question2)
    for result in results:
        print('{} -- {}'.format(result[0], result[1]))
    print('\n\n')

    #Error Percentage
    cursor.execute(answer3)
    results = cursor.fetchall()
    print(question3)
    for result in results:
        print("{} -- {:.2f}%".format(result[0], result[1]))
    print('\n')

    print('All questions answered')

if __name__ == '__main__':
    answers()
