#!/usr/bin/env python
import requests
import json

if __name__ == '__main__':
    hue_login_url = "http://192.168.235.130:8000/hue/accounts/login?username=hue&password=hue123"
    hue_list_databases_url = "http://192.168.235.130:8000/notebook/api/autocomplete/"
    login_response = requests.get(hue_login_url)
    # print(login_response.content)
    hue_login_cookies = requests.utils.dict_from_cookiejar(login_response.cookies)
    csrf_token = hue_login_cookies['csrftoken']
    # print(csrf_token)
    data = {
        "snippet": "{\"type\":\"presto\"}",
        "csrfmiddlewaretoken": csrf_token
    }
    list_databases_response = requests.post(hue_list_databases_url, cookies=hue_login_cookies,
                                            data=data).content
    print(list_databases_response)
