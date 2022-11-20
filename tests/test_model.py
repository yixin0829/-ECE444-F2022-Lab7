import pytest
from app import application, FakeNewsModel

@pytest.mark.parametrize("news, expected_code", [("Trump was a U.S. president", 0),
    ("Donald Trump is a women who was born in Bahama.", 1),
    ("Donald Trump Achieves World Peace!", 1),
    ("Elon Musk bought Google with 1$", 1)
    ])
def test_detector(news: str, expected_code: int):
    tester = application.test_client()
    fake_news_model = FakeNewsModel()
    fake_news_model.load_model()
    pred = fake_news_model.predict("Trump is dead.")
    assert pred == expected_code
    