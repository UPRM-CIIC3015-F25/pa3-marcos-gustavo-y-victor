from Cards.Card import Card, Rank

from enum import Enum

class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
class Card:
    def __init__(self, rank: Rank, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = rank.value


# DONE (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):
    ranks = []
    suits = []
    rank_counts = {}
    suits_counts = {}


    for card in hand:
        ranks.append(card.rank.value)
        suits.append(card.suit)

    for rank in ranks:
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1
    rank_values = sorted(rank_counts.values(), reverse=True)

    for suit in suits:
        if suit not in suits_counts:
            suits_counts[suit] = 1
        else:
            suits_counts[suit] += 1

    flush = False
    for count in suits_counts.values():
        if count >= 5:
            flush = True

    unique_ranks = sorted(set(ranks))
    if 14 in unique_ranks:
        unique_ranks.insert(0,1)
    straight = False
    for i in range(len(unique_ranks) - 4):
        if unique_ranks[i + 4] - unique_ranks[i] == 4:
            straight = True
            break

    suit_ranks = {}
    for card in hand:
        suit_ranks.setdefault(card.suit, []).append(card.rank.value)

    straight_flush = False
    for ranks_in_suit in suit_ranks.values():
        unique_suit_ranks = sorted(set(ranks_in_suit))
        if 14 in unique_suit_ranks:
            unique_suit_ranks.insert(0, 1)
        for i in range(len(unique_suit_ranks) - 4):
            if unique_suit_ranks[i + 4] - unique_suit_ranks[i] == 4:
                straight_flush = True
                break
        if straight_flush:
            break

    if straight_flush:
        return "Straight Flush"
    elif rank_values[0] == 4:
        return "Four of a Kind"
    elif len(rank_values) >= 2 and rank_values[0] == 3 and rank_values[1] == 2:
        return "Full House"
    elif flush:
        return "Flush"
    elif straight:
        return "Straight"
    elif rank_values[0] == 3:
        return "Three of a Kind"
    elif len(rank_values) >= 2 and rank_values[0] == 2 and rank_values[1] == 2:
        return "Two Pair"
    elif rank_values[0] == 2:
        return "One Pair"
    else:
        return "High Card"
