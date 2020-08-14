
def format_case(my_case):
    """
    This function format the cases, deleting the parentheses and generating groups based on the parentheses
    :param my_case: One of the cases from the input
    """
    arr = []
    group = []
    open = False
    for letter in my_case:
        if letter == '(':
            open = True
        elif open and letter == ')':
            arr.append(group)
            group = []
            open = False
        if open and letter != '(':
            group.append(letter)
        if open is not True and letter != ')':
            arr.append(letter)
    return arr


def count_match(arr, words, len_word):
    """
    This function count the matches case by case
    :param arr: case formatted in a array
    :param words: array of words
    :param len_word: length of word
    """
    counter = 0
    for word in words:
        checker = True
        for i in range(0, len_word):
            if word[i] not in arr[i]:
                checker = False
                break
        if checker:
            counter += 1
    return counter


def response_creator(cases, words, len_word, n_cases):
    response = []
    for i in range(0, n_cases):
        case_formatted = format_case(cases[i])
        matchs = count_match(case_formatted, words, len_word)
        response.append({"case": i + 1, "count": matchs})
    return response


def game():
    """
   Function for initialize the game, receiving the inputs and then return the results

    """
    print('Please enter the configuration numbers:')
    config = input()
    words = []
    cases = []

    try:

        config_arr = [int(x) for x in config.split()]
        len_word = config_arr[0]
        n_words = config_arr[1]
        n_cases = config_arr[2]
    except:
        print('wrong input, game over!')
        return
    for i in range(0, n_words):
        len_check = True
        print('Enter word:')
        while len_check:
            current_word = input()
            if len(current_word) == len_word:
                words.append(current_word)
                len_check = False
            else:
                print('Wrong length of word, enter again')

    for i in range(0, n_cases):
        print('Enter case:')
        current_case = input()
        cases.append(current_case)

    response = response_creator(cases, words, len_word, n_cases)
    for r in response:
        print('Case#' + str(r["case"]) + ':' + str(r["count"]))


game()
