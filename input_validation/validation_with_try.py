def average():
    # Get user input for scores
    score1 = input("Please enter a value for score 1: ")
    score2 = input("Please enter a value for score 2: ")
    score3 = input("Please enter a value for score 3: ")
    # Calculate and return average
    return (float(score1) + float(score2) + float(score3)) / 3


def average_try(score1, score2, score3):
    if float(score1) < 0:
        raise ValueError
    elif float(score2) < 0:
        raise ValueError
    elif float(score3) < 0:
        raise ValueError
    else:
        average_test_scores = (float(score1) + float(score2) + float(score3)) / 3
    return average_test_scores


if __name__ == '__main__':
    try:
        # Get user information
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")
        age = input("Please enter your age: ")
        score_one = input("Please enter a value for score 1: ")
        score_two = input("Please enter a value for score 2: ")
        score_three = input("Please enter a value for score 3: ")
        average_scores = average_try(score_one, score_two, score_three)
        # Format output and print to console
        print('{}, {} age: {} average grade: {:.2f}'.format(last_name, first_name, age, average_scores))
    except ValueError:
        print("Scores can't be negative")
