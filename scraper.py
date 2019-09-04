from bs4 import BeautifulSoup
import requests
import re


def get_all_links(url):
    result = []
    for a in _from(url).find_all('a'):
        link = a.get('href')
        if 'http' in link and 'nate.com' in link:
            result.append(link)
        else:
            result.append('https://pann.nate.com' + link)

    return _as_result(result)


def get_content(url):
    result = []
    for p in _from(url).find_all('p'):
        for text in _get_text(p):
            result.append(text)

    return _as_result(result)


def get_comments(url):
    result = []
    for dd in _from(url).find_all('dd'):
        for span in dd.find_all('span'):
            for text in _get_text(span):
                result.append(text)

    return _as_result(result)


def _get_text(element):
    text = element.get_text()
    text = text.replace('\xa0', ' ')
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    text = re.sub(r'[a-zA-Z_\\ ]+', ' ', text).strip()

    result = []
    for text in text.split('.'):
        result.append(text.strip())

    return result


def _from(url):
    response = requests.get(url)

    return BeautifulSoup(response.text, features='html.parser')


def _as_result(result):
    return list(filter(None, result))


# links = get_all_links('https://pann.nate.com')

print(get_comments('https://pann.nate.com/talk/347574107'))
