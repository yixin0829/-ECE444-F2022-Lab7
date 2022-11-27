import requests, json
import urllib.parse
from time import time

ENGPOINT = "http://lab7.eba-ficycrcw.us-east-2.elasticbeanstalk.com/"

def test_fake_news_api(text: str, call_times: int = 100) -> float:
    """call the api with input text. Return pred output (majority) and average latency over call_times times"""

    params = {'text': text}
    timer = [] # in ms
    preds = []

    for i in range(call_times):
        start_t = time()
        result = requests.get(f'{ENGPOINT}predict?{urllib.parse.urlencode(params)}')
        timer += [(time() - start_t)*1000] # in ms
        preds += [result.json().get('pred')]

    lis_mean = lambda l: sum(l) / len(l)
    print(f'mean predictions over {call_times} calls: {lis_mean(preds)}')
    print(f'mean latency over {call_times} calls: {lis_mean(timer)} ms')

    return lis_mean(preds), lis_mean(timer)

test_fake_news_api(text="Donald Trump was an U.S. president.") # expect: 0 (real)
test_fake_news_api(text="The Wall Street Journal is founded in 1889.") # expect: 0 (real)
test_fake_news_api(text="Donald Trump Achieves World Peace!") # expect: 1 (fake)
test_fake_news_api(text="Elon Musk bought Google with 1$") # expect: 1 (fake