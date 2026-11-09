import requests

def fun_call_list_api():
    url = f"http://127.0.0.1:8000/getitem/"
    response = requests.get(url)
    if response.status_code != 200:
        return ('Error')

    else:
        result = response.json()
        return(result)

def fun_call_add_item_api(newitem):
    url = f"http://127.0.0.1:8000/add/{newitem}"
    response = requests.post(url)
    if response.status_code != 200:
        return ('Error')

    else:
        result = response.json()
        return(result)

def fun_call_update_item_api(olditem, newitem):
    url = f"http://127.0.0.1:8000/updateitem/?olditem={olditem}&newitem={newitem}"
    response = requests.put(url)
    if response.status_code != 200:
        return ('Error')

    else:
        result = response.json()
        return(result)

def fun_call_delete_item_api(item):
    url = f"http://127.0.0.1:8000/deleteitam/?item={item}"
    response = requests.delete(url)
    if response.status_code != 200:
        return ('Error')

    else:
        result = response.json()
        return(result)
       
if __name__ == '__main__':
    fun_call_add_item_api(300)
    data = fun_call_list_api()
    print(data)

