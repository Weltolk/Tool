import requests
import datetime
import random
import time

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73", }


def loop(url: str, is_write: bool, is_print: bool) -> bool:
    prefix = "https://"
    domain = url
    if url[:7] == "http://":
        prefix = "http://"
        if url[-1:] == "/":
            domain = url[7:-1]
        else:
            domain = url[7:]
    elif url[:8] == "https://":
        if url[-1:] == "/":
            domain = url[8:-1]
        else:
            domain = url[8:]
    else:
        url = prefix + url
    # print(prefix)
    # print(domain)
    # print(url)
    session = requests.Session()
    result = session.get(url=url, headers=headers)
    session.close()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_text = now + " : " + prefix + domain + " : " + str(result.status_code) + "\n"
    if is_write:
        f = open(domain + ".txt", "a", encoding="utf-8")
        f.write(result_text)
        f.close()
    if is_print:
        print(result_text)
    return True


def random_sleep(start: int, stop: int) -> bool:
    print(time.time())
    time.sleep(random.randint(start, stop))
    print(time.time())
    return True


if __name__ == "__main__":
    baidu = "https://www.baidu.com/"
    bing = "https://cn.bing.com/"
    tencent_cloud = "https://cloud.tencent.com/"
    lol = "https://lol.qq.com/"
    while True:
        loop(baidu, True, True)
        loop(bing, True, True)
        loop(tencent_cloud, True, True)
        loop(lol, True, True)
        random_sleep(1, 1)
