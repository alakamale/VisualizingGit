import bq_helper
import os
import numpy as np
import pandas as pd
from google.cloud.bigquery.client import Client
import json
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='CA675-ede38ecf6679.json'
bq_client = Client()

github_repos = bq_helper.BigQueryHelper(active_project= "bigquery-public-data", 
                                       dataset_name = "github_repos")


query1= """SELECT size
            FROM `bigquery-public-data.github_repos.contents`
            WHERE binary = True
            LIMIT 5000
        """
github_repos.estimate_query_size(query1)
github_repo_sizes = github_repos.query_to_pandas_safe(query1, max_gb_scanned=2.34)
BYTES_PER_MB = 2**20

query9 ="""
        SELECT repo_name, watch_count
        FROM `bigquery-public-data.github_repos.sample_repos`
        ORDER BY watch_count DESC 
        LIMIT 2000
        """
data=github_repos.estimate_query_size(query9)
github_repo_trending_repos = github_repos.query_to_pandas_safe(query9)


with open('sorted_Languages_counts.json', 'r') as fp:
     sorted_Languages_counts = json.loads(fp.read())

query13 = """
WITH java_repos AS (
    SELECT DISTINCT repo_name -- Notice DISTINCT
    FROM `bigquery-public-data.github_repos.sample_files`
    WHERE path LIKE '%.java')
SELECT commits.repo_name, COUNT(commit) AS num_commits
FROM `bigquery-public-data.github_repos.sample_commits` AS commits
JOIN java_repos
    ON  java_repos.repo_name = commits.repo_name
GROUP BY commits.repo_name
ORDER BY num_commits DESC
"""
github_repo_num_java_distinct = github_repos.query_to_pandas_safe(query13, max_gb_scanned=5.3)


df = pd.read_csv('Language.csv')
df =df.truncate(after=381)







##########
data1 = github_repo_sizes.divide(BYTES_PER_MB)
data2 = github_repo_trending_repos[:20]
data3 = github_repo_num_java_distinct
data4 = df
language = list(zip(*sorted_Languages_counts[:15]))[0]
count = list(zip(*sorted_Languages_counts[:15]))[1]
x_pos = np.arange(len(language))