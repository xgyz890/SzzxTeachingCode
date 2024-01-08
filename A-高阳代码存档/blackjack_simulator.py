# coding=utf-8

import random
import multiprocessing
import math
import timeit

simulations = 600000
num_decks = 4
shuffle_perc = 75

def simulate(queue, batch_size):

    deck = []

    def new_deck():
        std_deck = [
           #2 3 4 5 6 7 8 9 10 J  Q  K  A
            2,3,4,5,6,7,8,9,10,10,10,10,11,
            2,3,4,5,6,7,8,9,10,10,10,10,11,
            2,3,4,5,6,7,8,9,10,10,10,10,11,
            2,3,4,5,6,7,8,9,10,10,10,10,11,
        ]
        std_deck = std_deck * num_decks
        random.shuffle(std_deck)
        return std_deck[:]  # so we have a copy of deck to work on, and the original deck remains intact

    def play_hand():
        dealer_cards = []
        player_cards = []

        player_cards.append(deck.pop(0))
        dealer_cards.append(deck.pop(0))
        player_cards.append(deck.pop(0))
        dealer_cards.append(deck.pop(0))

        while sum(player_cards) < 12:
            player_cards.append(deck.pop(0))

        while sum(dealer_cards) < 18:
            exit = False

            # check for soft 17, replace A with 1.
            if sum(dealer_cards) == 17:
                exit = True
                for i,card in enumerate(dealer_cards):
                    if card == 11:
                        exit = False
                        dealer_cards[i] = 1

            if exit:
                break

            dealer_cards.append(deck.pop(0))

        player_sum = sum(player_cards)
        dealer_sum = sum(dealer_cards)

        if dealer_sum > 21:
            return 1
        elif dealer_sum == player_sum:
            return 0
        elif dealer_sum > player_sum:
            return -1
        elif dealer_sum < player_sum:
            return 1

    # Use play_hand() to play the game over and over as the simulation.

    deck = new_deck()

    win = 0
    draw = 0
    lose = 0
    for i in range(batch_size):

        if float(len(deck) / (52 * num_decks)) * 100 < shuffle_perc:
            deck = new_deck()

        result = play_hand()

        if result == 1:
            win += 1
        elif result == 0:
            draw += 1
        elif result == -1:
            lose += 1

    queue.put([win, draw, lose])

    # (end of simulate())

# Need to put the multiprocessing inside:
#
# if __name__ == "__main__":
#
# to run it properly.

# 详细解释：
# 由于Python运行过程中，新创建进程后，进程会导入正在运行的文件，即在运行代码0.1的时候，代码在运行到mp.Process时，
# 新的进程会重新读入改代码。对于没有if __name__=="__main__"保护的代码，新进程都认为是要再次运行的代码，
# 这是子进程又一次运行mp.Process，但是在multiprocessing.Process的源码中是对子进程再次产生子进程是做了限制的，
# 是不允许的，于是出现如上的错误提示。
# 来自：https://www.cnblogs.com/wFrancow/p/8511711.html


if __name__ == "__main__":

    start = timeit.default_timer()

    cpus = multiprocessing.cpu_count()
    batch_size = int(math.ceil(simulations / float(cpus)))

    queue = multiprocessing.Queue()
    processes = []
    for i in range(cpus):
        process = multiprocessing.Process(target=simulate, args=(queue, batch_size))
        processes.append(process)
        process.start()

    for proc in processes:
        proc.join()

    finish_time = timeit.default_timer() - start

    win = 0
    draw = 0
    lose = 0

    for i in range(cpus):
        results = queue.get()
        win += results[0]
        draw += results[1]
        lose += results[2]

    print("Core used: {}".format(cpus))
    print("total simulations: {}".format(simulations))
    print("simulations per sec: {:.0f}".format(float(simulations / (finish_time))))
    print("execution time: {:.3} seconds".format(finish_time))
    print("win percentage: {:.2f}%".format(float(win / simulations * 100)))
    print("draw percentage: {:.2f}%".format(float(draw / simulations * 100)))
    print("lose percentage: {:.2f}%".format(float(lose / simulations * 100)))
