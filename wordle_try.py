import random

def random_answer():
    word_list = []
    word_file = open("words.txt")
    for word in word_file:
        word_list.append(word.strip())
    answer = random.choice(word_list)
    return answer.upper()

def display_hint(hint):
    print(" ".join(hint))

def main():
    is_running = True
    try_again = True
    while try_again:
        answer = random_answer()
        hint = ["_"] * len(answer)
        display_hint(hint)
        mistakes = 0
        while is_running:

            if "_" in hint:
                mistakes += 1
                guess = input("Guess :").upper()
                if "_" in hint:
                    for i in range(len(answer)):
                        for n in range(len(guess)):
                            if guess[n] == answer[i]:
                             hint[i] = guess[n]
                    display_hint(hint)
            else :

                print(f"{answer} Was right ")
                is_running = False
                print(f"You Win!\nİt took {mistakes}try")
        if not is_running:
            again = input("Try Again ?(y/n)")
            if again == "y" or again == "Y":

                is_running = True
                try_again = True
            else:
                try_again = False
main()