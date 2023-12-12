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
        print("========")
        steps_to_loose += 1
        current_funds -= current_bet
        print(f"{current_funds=}", f"{current_bet=}")
        flipped_coin_value = flip_coin()
        print(f"flipped_coin_value: {flipped_coin_value}")
        if flipped_coin_value == HEADS:
            win = current_bet * 2
            print(f"{win=}")
            current_funds += current_bet * 2
            current_bet = min_bet
        else:
            print("loose")
            current_bet *= 2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds
    return steps_to_loose


print(play_martingale(starting_funds=100, min_bet=1, max_bet=100))


def simulate_martingale_for_n_games(starting_funds: int, min_bet: int, max_bet: int, n_games: int) -> float:
    total_steps_to_loose = 0
    for i in range(n_games):
        step_to_loose = play_martingale(starting_funds, min_bet, max_bet)
        total_steps_to_loose += step_to_loose
    return total_steps_to_loose / n_games
