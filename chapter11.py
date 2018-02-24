import requests # http://requests.readthedocs.io/en/master/

res= requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
print(res.text[:250])

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))


playFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
        playFile.write(chunk)

playFile.close()