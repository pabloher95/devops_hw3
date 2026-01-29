from app import app, dice_art, coin_art
import pytest
from unittest.mock import patch


@pytest.fixture
def app_tester():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_rpswin(app_tester):
    user_choice = "scissors"
    pc_choice = "paper"

    with patch("random.choice", return_value=pc_choice):
        response = app_tester.get(f"/rps?choice={user_choice}")
        data = response.get_json()
    assert data["user"] == user_choice
    assert data["pc"] == pc_choice
    assert data["result"] == "win"


def test_rpsloss(app_tester):
    user_choice = "rock"
    pc_choice = "paper"

    with patch("random.choice", return_value=pc_choice):
        response = app_tester.get(f"/rps?choice={user_choice}")
        data = response.get_json()
    assert data["user"] == user_choice
    assert data["pc"] == pc_choice
    assert data["result"] == "lose"


def test_rpsdraw(app_tester):
    user_choice = "paper"
    pc_choice = "paper"

    with patch("random.choice", return_value=pc_choice):
        response = app_tester.get(f"/rps?choice={user_choice}")
        data = response.get_json()
    assert data["user"] == user_choice
    assert data["pc"] == pc_choice
    assert data["result"] == "draw"


def test_diceshape(app_tester):
    with patch("random.randint", return_value=6):
        response = app_tester.get("/diceroll")
        text = response.data.decode("utf-8")
    assert "Dice Roll: 6" in text
    for line in dice_art[6]:
        assert line in text


def test_cointoss(app_tester):
    with patch("random.randint", return_value=1):
        response = app_tester.get("/coinflip")
        text = response.data.decode("utf-8")
    assert "Coin Flip: Tail" in text
    for line in coin_art[1]:
        assert line in text
