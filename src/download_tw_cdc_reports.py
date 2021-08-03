import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from os import path

CDC_BASE_URL = "https://www.cdc.gov.tw"
REPORTS_URL = "https://www.cdc.gov.tw/Category/Page/9jFXNbCe-sFK9EImRRi2Og"

WEEKLY_DIR = "data/pdf/weekly/"
DAILY_DIR = "data/pdf/daily/"
ADVERSE_DIR = "data/pdf/adverse_events/"

SAVE_VIEWER_HTML = False


class UnknownDownloadLinkException(Exception):
    pass


def is_daily(name: str):
    return name.endswith("疫苗接種統計資料.pdf") or name.endswith("疫苗日報表.pdf")


def is_weekly(name: str):
    return name.endswith("疫苗接種對象累計接種人次.pdf")


def is_adverse_event(name: str):
    return name.endswith("疫苗接種後不良反應事件通報.pdf")


def download_cdc_reports():
    reports_page = requests.get(REPORTS_URL)
    links: ResultSet[Tag] = BeautifulSoup(
        reports_page.content, "html.parser", from_encoding="utf-8").select("div.download a")

    for link in links:
        file_name = link.get_text()
        if is_daily(file_name):
            file_path = DAILY_DIR + file_name
        elif is_weekly(file_name):
            file_path = WEEKLY_DIR + file_name
        elif is_adverse_event(file_name):
            file_path = ADVERSE_DIR + file_name
        else:
            raise UnknownDownloadLinkException(
                "Unknown download category:" + file_name)

        file_path = path.abspath(file_path)
        if path.exists(file_path) and path.getsize(file_path) > 1024:
            print(file_name + " exists, size=" + str(path.getsize(file_path)))
        else:
            print(file_path, "does not exist")
            viewer_url = CDC_BASE_URL + link['href']
            print("fetching viewer html:", viewer_url)
            viewer_page = requests.get(viewer_url)
            print("headers:", viewer_page.headers)
            print("encoding:", viewer_page.encoding)
            print("apparent encoding:", viewer_page.apparent_encoding)
            #viewer_page.encoding = viewer_page.apparent_encoding
            print(viewer_page.content)
            if SAVE_VIEWER_HTML:
                print(viewer_page.content)
                with open(file_path+".html", 'wb') as f:
                    f.write(viewer_page.content)

            pdf_link: ResultSet[Tag] = BeautifulSoup(
                viewer_page.content,  "html.parser", from_encoding="utf-8").select("a.nav-link")[0]
            pdf_url = CDC_BASE_URL + pdf_link['href']
            print("fetching pdf:", pdf_url)
            print("saving file to:", file_path)
            with open(file_path, 'wb') as f:
                f.write(requests.get(pdf_url).content)


download_cdc_reports()
