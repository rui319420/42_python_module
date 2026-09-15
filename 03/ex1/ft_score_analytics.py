import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    score_list = []
    error_occurred = 0
    for arg in sys.argv[1:]:
        try:
            score_list.append(int(arg))
        except ValueError as e:
            print(f"Invalid parameter: {arg}")
            error_occurred = 1
    total_players = len(score_list)
    if (error_occurred == 1) | (total_players == 0):
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ...")
        return

    print(f"Scores processed: {score_list}")
    print(f"Total players: {total_players}")
    print(f"Total score: {sum(score_list)}")
    print(f"Average score: {sum(score_list) / total_players}")
    print(f"High score: {max(score_list)}")
    print(f"Low score: {min(score_list)}")
    print(f"Score range: {max(score_list) - min(score_list)}")


if __name__ == "__main__":
    main()
