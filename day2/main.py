import sys

if __name__ == '__main__':
    possible_games_1 = {
        "A X": 1 + 3,  # rock rock => draw
        "A Y": 2 + 6,  # rock paper => win
        "A Z": 3 + 0,  # rock scissors => lose
        "B X": 1 + 0,  # paper rock => lose
        "B Y": 2 + 3,  # paper paper => draw
        "B Z": 3 + 6,  # paper scissors => win
        "C X": 1 + 6,  # scissors rock => win
        "C Y": 2 + 0,  # scissors paper => lose
        "C Z": 3 + 3,  # scissors scissors => draw
    }

    possible_games_2 = {
        "A X": 0 + 3,  # rock lose => scissors
        "A Y": 3 + 1,  # rock draw => rock
        "A Z": 6 + 2,  # rock win => paper
        "B X": 0 + 1,  # paper lose => rock
        "B Y": 3 + 2,  # paper draw => paper
        "B Z": 6 + 3,  # paper win => scissors
        "C X": 0 + 2,  # scissors lose => paper
        "C Y": 3 + 3,  # scissors draw => scissors
        "C Z": 6 + 1,  # scissors win => rock
    }

    games = (l.strip() for l in open(sys.argv[1]))
    score_1 = 0
    score_2 = 0
    for g in games:
        score_1 += possible_games_1[g]
        score_2 += possible_games_2[g]

    print("Part 1:", score_1)
    print("Part 2:", score_2)


