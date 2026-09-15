import sys


class NoScoreError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


def analytics_arguments(args: list) -> int:
    return len(sys.argv[1:])


def main() -> None:
    print("=== Player Score Analytics ===")
    total_players = len(sys.argv[1:])
    if total_players == 0:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    score_list = [0] * total_players
    i = 0
    for arg in sys.argv[1:]:
        score_list[i] = int(arg)
        i += 1
    print(f"Scores processed: {score_list}")
    print(f"Total players: {total_players}")
    print(f"Total score: {sum(score_list)}")
    print(f"Average score: {sum(score_list) / total_players}")
    print(f"High score: {max(score_list)}")
    print(f"Low score: {min(score_list)}")
    print(f"Score range: {max(score_list) - min(score_list)}")


if __name__ == "__main__":
    main()
