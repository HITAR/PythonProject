import requests

def download(url):
    res = requests.get(url)
    if res.status_code == 404:
        print("Not Found.")
        return
    filename = url.split('/')[-1]
    with open(filename,'wb') as fobj:
        fobj.write(res.content)
    print("Succeed.")

if __name__ == '__main__':
    download(input("Input URL:"))
