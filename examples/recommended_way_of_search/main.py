from pymed import PubMed
import pandas as pd
import datetime
import time
import json

pubmed = PubMed(tool="toolname", email="your email")

# Timer
start_time = time.time()

industryList = []  # Array of companys

for comp in industryList:
    comp_time = time.time()
    articleList = []
    articleInfo = []
    query = f"your test query here with {comp}, same as how pubmed takes the queries"
    results = pubmed.query(query, max_results=999999)
    for article in results:
        articleDict = article.toDict()
        articleList.append(articleDict)
    for article in articleList:
        articleInfo.append({'pubmed_id': article['pubmed_id'],
                            'title': article['title'],
                            'keywords': article['keywords'],
                            'mesh': article['mesh'],
                            'journal': article['journal'],
                            'abstract': article['abstract'],
                            'conclusions': article['conclusions'],
                            'methods': article['methods'],
                            'results': article['results'],
                            'copyrights': article['copyrights'],
                            'doi': article['doi'],
                            'references': article['references'],
                            'publication_date': str(article['publication_date']),
                            'authors': article['authors']})

    # Export to both CSV and .txt files
    articlesPD = pd.DataFrame.from_dict(articleInfo)
    export_csv = articlesPD.to_csv(
        f'Pubmed_DataFrame_{comp}.csv', index=None, header=True)
    with open(f"PubMed_JSON_{comp}.txt", "w") as outfile:
        json.dump(articleInfo, outfile)

    # Print time it took program to run said company files
    print(f"{comp} DataFrame Done in {(time.time() - comp_time)} seconds OR {((time.time() - comp_time) / 60)} minutes")

# Print time it took to run script
print(
    f"Full execution took {(time.time() - start_time)} seconds OR {((time.time() - comp_time) / 60)} minutes")
print("done")
