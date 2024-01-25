import requests

if __name__ == '__main__':
    url = 'httpbin.org.get'
    args = {'nombre': 'Agustin', 'curso': 'python'}

    response = requests.get(url, params=args)

    if response.status_code == 200:
        content = response.content
        print(content)
