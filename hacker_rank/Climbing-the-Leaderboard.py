from bisect import bisect_right, insort_right


scores = list(map(int, '100 100 50 40 40 20 10'.split()))
alice = list(map(int, '5 25 50 120'.split()))


def climbingLeaderboard(scores, alice):
    # List to contain and return Alice's ranks.
    results = []

    # Unique values from scores, since duplicate scores will have same rank (their index value).
    leaderboard = sorted(set(scores), reverse=True)

    # Use this var to track index within leaderboard later.
    l = len(leaderboard)

    # Loop through each of Alice's scores
    for a in alice:
        print(a, end='....')

        # If Alice's score is >= the score at the index of the end of leaderboard...
        # Subtract 1 from that index value (which is also the rank) to check the next score up.
        # If the score is less than the next score up, the index (rank) will be added to results.
        while (l > 0) and (a >= leaderboard[l - 1]):
            print(a, leaderboard[l - 1], l)
            l -= 1

        # We add 1 to the appended value to account for 0-indexing.
        results.append(l + 1)

    print(results)
    return results


    # output = []
    # for score in alice:
    #     insort_right(scores, score)
    #     # print(scores)
    #     filtered_rank = list(sorted(set(scores), reverse=True))
    #     # print(filtered_rank)
    #     filtered_rank.sort(reverse=True)
    #     rank = filtered_rank.index(score)+1
    #     index = filtered_rank.index(score)
    #     # print(index, rank)
    #     output.append(rank)
    #     scores.remove(score)
    #     # print(scores)
    #
    #
    # print(output)
    # return output

if __name__ == '__main__':
    climbingLeaderboard(scores, alice)