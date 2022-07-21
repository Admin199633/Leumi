
import requests
import datetime
from datetime import datetime
import csv
# Change base URL
JIRA_HOST = "http://localhost:8080"

# Change credentials
CREDENTIALS = ('lior', '123456')

headers = {
'X-Atlassian-Token': 'no-check'

}
payload = {
    'filterParameters': '{"groups":["jira-software-users"],"userStatus":"ACTIVE"}'
}
files = {'filterParameters': (None, '')}

r = requests.post(JIRA_HOST + '/rest/techtime-usermanagement/1.0/bulkChange/userFilter', files=files, data=payload,
                  timeout=2.5, headers=headers, auth=CREDENTIALS, )
read=r.json()
print(read)





values = [i['lastLogin'] for i in read]
print(values)

for i in range(len(values)):
    if values[i] != 0:
         values[i] = datetime.fromtimestamp(values[i]/1000)
         print([values[i]])


for i in range(len(values)):
    read[i]['lastLogin'] = values[i]


print(datetime.fromtimestamp(1658401826.428))
#
with open('4.csv', 'w',newline="") as output_file:
    writer = csv.writer(output_file, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(list(read[0].keys()))
    for i in range(len(read)):
        new_row = map(lambda x: str(x), list(read[i].values()))
        writer.writerow(new_row)
    print("HEll")

# print(list(read[0].keys()))
