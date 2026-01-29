# DevOps HW3

This very simple Flask web application was developed to showcase CI functionalities using Github Actions. The minimum requirement is to have [`uv` installed](https://docs.astral.sh/uv/getting-started/installation/) to manage the python environment.


To deploy the app locally, clone the repo and execute the following code from the repo's root directory: 

```
uv sync

uv run app.py
```

Once the app is served, follow this link: `http://localhost:8000/` and verify that you can see a message that reads: `Hello from Flask!`

 The app is composed of  three endpoints, each containing a game: 

#### Rock, paper, scissors (/rps)
In this game, the user plays a strategy (`rock`, `paper` or `scissors`) using the following query format: 

`http://localhost:8000/rps?choice={strategy}`

The endpoint generates a random strategy for the computer, compares the two strategies and returns an outcome among `draw`, `win` or `lose`. 

#### Dice roll (/diceroll)
In this game, a dice is rolled by picking a random number between 1 and 6 every time the endpoint is visited and rendering the value as well as a utf-8 graphic representation of the outcome: 

`http://localhost:8000/diceroll`

#### Coin flip (/coinflip)
In this game, a coin is tossed by picking a random number between 0 (heads) and 1 (tails) every time the endpoint is visited and rendering the value as well as a utf-8 graphic representation of the outcome: 

`http://localhost:8000/`

The app's test suite can be run locally using the following command:
`uv run pytest test_app.py`