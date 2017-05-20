import psycopg2
DB_NAME = "news"

# 1. What are the most popular three articles of all time?
query1 = "select title, count(*) as views from articles,log where log.path like concat('%',articles.slug,'%') group by articles.title order by views desc"

# 2. Who are the most popular article authors of all time?
query2 = ""

# 3. On which days did more than 1% of requests lead to errors?
query3 = ""

# to store results
query_1_result = dict()
query_1_result['title'] = "The 3 most popular articles of all time are:"

query_2_result = dict()
query_2_result['title'] = "The most popular article authors of all time are:"

query_3_result = dict()
query_3_result['title'] = "Days with more than 1%% of request that lead to an error:"


# returns query result
def get_query_result(query):
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

def print_query_results(query_result):
    print query_result['title']
    for result in query_result['results']:
        print result[i]

# stores query result and print formatted output
query_1_result['results'] = get_query_result(query1)
print_query_results(query_1_result)
