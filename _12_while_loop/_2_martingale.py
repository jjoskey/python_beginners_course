import random

HEADS = "heads"
TAILS = "tails"
COIN_VALUES = [HEADS, TAILS]


def flip_coin():
    return random.choice(COIN_VALUES)


def play_martingale(starting_funds: int, min_bet: int, max_bet: int) -> int:
    steps_to_loose = 0
    current_funds = starting_funds
    current_bet = min_bet
    while current_funds > 0:
        steps_to_loose += 1
        current_funds -= current_bet
        if flip_coin() == HEADS:
            current_funds += current_bet * 2
            current_bet = min_bet
        else:
            current_bet *= 2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds
    return steps_to_loose


def simulate_martingale_for_n_games(starting_funds: int, min_bet: int, max_bet: int, n_games: int) -> float:
    total_steps_to_loose = 0
    for _ in range(n_games):
        step_to_loose = play_martingale(starting_funds, min_bet, max_bet)
        total_steps_to_loose += step_to_loose
    return total_steps_to_loose / n_games


print(simulate_martingale_for_n_games(starting_funds=100, min_bet=1, max_bet=20, n_games=10))
