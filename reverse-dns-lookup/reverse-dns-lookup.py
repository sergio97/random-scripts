import requests
import bs4


IPS = [
    '128.100.100.120',
    '128.100.100.121',
    '128.100.100.122',
    '128.100.100.123',
    '128.100.100.124',
    '128.100.100.125',
    '128.100.100.126',
    '128.100.100.127',
    '128.100.100.128',
    '128.100.100.129',
    '128.100.100.130',
]
HEADERS = {
    'content-type': 'application/x-www-form-urlencoded',
    'DNT': '1',
    'referer': 'http://remote.12dt.com/lookup.php',
    'host': 'remote.12dt.com',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0',
}


for ip in IPS:
    response = requests.post(
        url="http://remote.12dt.com/lookup.php",
        data=f'ip={ip}&Submit=Lookup'.encode('ascii'),
        headers=HEADERS
    )
    assert response.status_code == 200

    # with open('/tmp/debug.html', 'wb') as f:
    #     f.write(response.content)

    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    result = soup.find('div', 'results')
    assert result

    dns_name = result.get_text().split('"')[1]
    print(f'{ip}: {dns_name}')
