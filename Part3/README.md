## Log Analysis.

The project here answers several different types of questions.

## Files

* `logAnalysis.py` -- The actual python code which runs different queries to answer the questions.
* `output.txt` -- The output that we get.

## Usage

1. Boot up virtual machine using **vagrant up**.
2. Login using **vagrant ssh**.
3. cd /vagrant.
4. run **python `logAnalysis.py`**.
5. The output of the queries we ran to get answers.


## Description
The `answers()` function is called from `__main__` inside which all the queries are run
in a order to output all the asked questions.


## Views in project

1. top_articles
```
CREATE VIEW top_articles AS
SELECT title, author, count(title) AS num FROM articles, log
WHERE log.path = concat('/article/', articles.slug)
GROUP BY articles.title, articles.author
ORDER BY num DESC;
```

2. top_authors
```
CREATE VIEW top_authors AS
SELECT name, sum(top_articles.num) AS total FROM top_articles, authors
WHERE authors.id = top_articles.author
GROUP BY authors.name
ORDER BY total DESC;
```

3. all_requests
```
CREATE VIEW all_requests AS SELECT date(TIME) AS date, count(*) AS num FROM log
GROUP BY date
ORDER BY num DESC;
```

4. error_requests
```
CREATE VIEW error_requests AS SELECT date(TIME) AS date, count(*) AS num FROM log
WHERE status = '404 NOT FOUND'
GROUP BY date
ORDER BY num DESC;
```

5. error_percentage
```
CREATE VIEW error_percentage AS SELECT all_requests.date, (100.0*error_requests.num/all_requests.num) AS error_rate FROM all_requests, error_requests WHERE all_requests.date = error_requests.date;
```
