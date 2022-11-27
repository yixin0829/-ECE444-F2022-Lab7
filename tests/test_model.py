import pytest
from app import application, FakeNewsModel

@pytest.mark.parametrize("news, expected_code", [("Donald Trump was an U.S. president", 0),
    ("Real News.", 0),
    ("Donald Trump Achieves World Peace!", 1),
    ("Elon Musk bought Google with 1$", 1)
    ])
def test_detector(news: str, expected_code: int):
    tester = application.test_client()
    fake_news_model = FakeNewsModel()
    pred = fake_news_model.predict(news)
    assert pred == expected_code
    