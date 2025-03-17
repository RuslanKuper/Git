import requests
import pytest

url = 'https://ru.yougile.com'
headers = {
    'Authorization':
    'Bearer CIhOuA1z5iv-E5uJlvqS6cgoIAvH2RB3oej7RaF7CbHnKPcDrERmerl8TOqRHxJ8'
}


# tests_boards
def test_status_code():
    response = requests.get(url + '/api-v2/boards?limit=50&offset=0',
                            headers=headers)
    assert response.status_code == 200


def test_create_board():
    response_create_board = requests.post(
        url + '/api-v2/boards',
        headers=headers,
        json={
            "title": "Board_1",
            "projectId": "039c400d-c3b4-4634-92c3-d009d6158193"
        })
    assert response_create_board.status_code == 201


def test_get_board_ID():
    response_test_get_board_ID = requests.get(
        url + '/api-v2/boards/b0781859-2e22-40f3-9653-226d550ddb60',
        headers=headers)
    assert response_test_get_board_ID.status_code == 200


def test_update_board():
    response_test_update_board = requests.put(
        url + '/api-v2/boards/66c17058-28a0-477a-8bbf-a2d0eb2270a7',
        headers=headers,
        json={
            "title": "+17",
            "projectId": "039c400d-c3b4-4634-92c3-d009d6158193"
        })
    assert response_test_update_board.status_code == 200


# tests_columns
def test_response_columns():
    response_columns = requests.get(url + '/api-v2/columns?limit=50&offset=0',
                                    headers=headers)
    assert response_columns.status_code == 200


def test_response_create_columns():
    response_test_response_create_columns = requests.post(
        url + '/api-v2/columns',
        headers=headers,
        json={
            "title": "Columns+3",
            "color": 4,
            "boardId": "ec4f39c2-c57c-420d-8b40-03332f0c3955"
        })
    assert response_test_response_create_columns.status_code == 201


def test_response_id():
    test_response_id = requests.get(
        url + '/api-v2/columns/ff07f0a6-6810-4a72-a24b-146d809a780c',
        headers=headers)
    assert test_response_id.status_code == 200

def test_response_column_update():
    test_response_column_update = requests.put(url + '/api-v2/columns/ff07f0a6-6810-4a72-a24b-146d809a780c', headers = headers, json={
  "title": "Columns+Hello1111",
  "color": 2,
  "boardId": "548e4e4a-5eec-4820-a01b-f98302ecc862"
}) 
    assert test_response_column_update.status_code == 200

# collection tasks


def test_response_tasks():
    test_response_tasks = requests.get(url + '/api-v2/tasks?limit=50&offset=0', headers = headers)

    assert test_response_tasks.status_code == 200


def test_response_create_tasks():
    test_response_create_tasks = requests.post(url + '/api-v2/tasks', headers = headers, json = {
    "title": "TASKA+задача",
    "columnId": "ff07f0a6-6810-4a72-a24b-146d809a780c"
})
    assert test_response_create_tasks.status_code == 201    


def test_response_tasks_id():
    test_response_tasks_id = requests.get(url + '/api-v2/tasks/d09f2dfe-d86f-4fbe-92fc-b46ffe813fae', headers = headers)
    assert test_response_tasks_id.status_code == 200


def test_response_tasks_update():
    test_response_tasks_update = requests.put(url + '/api-v2/tasks/d09f2dfe-d86f-4fbe-92fc-b46ffe813fae', headers = headers, json={
    "title": "New/Новая задача",
  "columnId": "ff07f0a6-6810-4a72-a24b-146d809a780c"
})
    assert  test_response_tasks_update.status_code == 200