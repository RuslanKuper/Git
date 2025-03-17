import requests
import json

url = 'https://ru.yougile.com'

headers = {
    'Authorization': 'Bearer CIhOuA1z5iv-E5uJlvqS6cgoIAvH2RB3oej7RaF7CbHnKPcDrERmerl8TOqRHxJ8'
}
# collection Boards

response = requests.get(url + '/api-v2/boards?limit=50&offset=0', headers = headers)

if response.status_code == 200:
    response_pretty = json.dumps(response.json(), indent = 4, ensure_ascii = False)
    print(response_pretty, response.status_code)

else:
    print('not ok')

response_create_board = requests.post(url + '/api-v2/boards', headers = headers, json={
    "title": "Доска 6666666",
    "projectId": "039c400d-c3b4-4634-92c3-d009d6158193"
})

if response.status_code == 201:
    response_pretty = json.dumps(response_create_board.json(), indent = 4, ensure_ascii = False)
    print(response_pretty, response_create_board.status_code)

else:
    print('not ok')

response = requests.get(url + '/api-v2/boards/b0781859-2e22-40f3-9653-226d550ddb60', headers = headers)
if response.status_code == 200:
        response_pretty = json.dumps(response.json(),indent = 4, ensure_ascii= False)
        print(response_pretty, response.status_code)
else:
        print('not ok')

response = requests.put(url + '/api-v2/boards/1994b796-e6e9-41ba-8c0f-c3ec4b695e25',headers = headers, json={
    "title": "+1",
    "projectId": "039c400d-c3b4-4634-92c3-d009d6158193"})

if response.status_code == 200:
         response_pretty = json.dumps(response.json(),indent = 4, ensure_ascii= False)
         print(response_pretty, response.status_code)
else:
        print('not ok')

# collection columns

response_columns = requests.get(url + '/api-v2/columns?limit=50&offset=0', headers = headers)
if response.status_code == 200:
        response_pretty = json.dumps(response.json(),indent = 4, ensure_ascii= False)
        print(response_pretty, response_columns.status_code)
else:
        print('not ok')


response_create_columns = requests.post(url + '/api-v2/columns' ,headers = headers, json={
  "title": "Columns+2",
  "color": 1,
  "boardId": "ec4f39c2-c57c-420d-8b40-03332f0c3955"
})

response = requests.get(url + '/api-v2/columns/ff07f0a6-6810-4a72-a24b-146d809a780c', headers = headers)
if response.status_code == 200:
        response_pretty = json.dumps(response.json(),indent = 4, ensure_ascii= False)
        print(response_pretty, response.status_code)
else:
        print('not ok')

response = requests.put(url + '/api-v2/columns/ff07f0a6-6810-4a72-a24b-146d809a780c', headers = headers, json={
  "title": "Columns+Hello",
  "color": 2,
  "boardId": "548e4e4a-5eec-4820-a01b-f98302ecc862"
})
if response.status_code == 200:
         response_pretty = json.dumps(response.json(),indent = 4, ensure_ascii= False)
         print(response_pretty, response.status_code)
else:
        print('not ok')

# collection tasks

response_tasks = requests.get(url + '/api-v2/tasks?limit=50&offset=0', headers = headers)
if response.status_code == 200:
        response_pretty = json.dumps(response.json(),indent = 4, ensure_ascii= False)
        print(response_pretty, response_tasks.status_code)
else:
        print('not ok')

response_create_tasks = requests.post(url + '/api-v2/tasks', headers = headers, json = {
    "title": "TASKA+задача",
    "columnId": "ff07f0a6-6810-4a72-a24b-146d809a780c"
})

response_tasks_id = requests.get(url + '/api-v2/tasks/d09f2dfe-d86f-4fbe-92fc-b46ffe813fae', headers = headers)
if response.status_code == 200:
        response_pretty = json.dumps(response.json(),indent = 4, ensure_ascii= False)
        print(response_pretty, response_tasks_id.status_code)
else:
        print('not ok')

response_tasks_put = requests.put(url + '/api-v2/tasks/d09f2dfe-d86f-4fbe-92fc-b46ffe813fae', headers = headers, json={
    "title": "New/Новая задача",
  "columnId": "ff07f0a6-6810-4a72-a24b-146d809a780c"
})
if response.status_code == 200:
        response_pretty = json.dumps(response.json(),indent = 4, ensure_ascii= False)
        print(response_pretty, response_tasks_put.status_code)
else:
        print('not ok')