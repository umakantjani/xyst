import requests
import json

api = "https://public.tableau.com/api/search/query?language=en-us&type=vizzes"
print( "*"*30 + "\n" + "Welcome to Pivotis Web Scraper!"+ "\n" + "*"*30)

query_string = input("Please enter the keyword you want to search for! ")
total_workbooks = input("How many workbook search results you're looking for? ")

#this is a condition to give that user should not provide the total_workbooks nbumber more than 10,000 as Tableau's server only limits to 10,000 requests every 24 hour
if int(total_workbooks) >= 10000:
    total_workbooks = input("Tableau only allows 10,000 requests per 24 hours please select a number smallaer than 10,000. /n please enter number of workbook search results you're searching for: ")
else:
    if int(total_workbooks) <= 100:
        outrange = 1
        iCount=int(total_workbooks)
    else:
        outrange = int(int(total_workbooks)/100)
        iCount=100

    #start point is the range selector
    start_point=0

    for i in range(0, outrange):
        make_the_request = api + "&query=" + str(query_string) + "&start=" + str(start_point) + "&count=" + str(iCount)
        response = requests.get(make_the_request)
        start_point=+100

        #check the response of the requests
        if response.status_code!=200:
            print("Something is not right. /n Error Output from Server:" + response.status_code)
        else:
            data = response.json()

            if i<=9:
                wbs_output = "wbs_output0"+ str(i)
            else:
                wbs_output = "wbs_output"+ str(i)

            #print(data)
            with open('outputs/wbs_output.json', 'w') as outf:
                outf.write(json.dumps(data))
