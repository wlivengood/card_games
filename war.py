import random, time

class Card:
    RANKS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
    SUITS = ["clubs", "diamonds", "hearts", "spades"]
    def __init__(self, rank, suit):
        if rank < 2 or rank > 14:
            raise RuntimeError("Invalid Rank")
        if suit > 3:
            raise RuntimeError("Invalid Suit")
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return self.RANKS[self.rank] + " of " + self.SUITS[self.suit]
    def __lt__(self, other):
        return self.rank < other.rank
    def __le__(self, other):
        return self.rank <= other.rank
    def __eq__(self, other):
        return self.rank == other.rank
    def __ne__(self, other):
        return self.rank != other.rank
    def __ge__(self, other):
        return self.rank >= other.rank
    def __gt__(self, other):
        return self.rank > other.rank

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in range(4) for rank in \
                      range(2, 15)]
    def __str__(self):
        s = ""
        for card in self.cards:
            s += str(card) + "\n"
        return s
    def shuffle(self):
        random.shuffle(self.cards)
    def is_empty(self):
        return not self.cards
    def deal(self, hands, number):
        for i in range(len(hands)):
            if self.is_empty():
                break
            else:
                [hands[i % len(hands)].pickup(self.cards.pop()) \
                 for i in range(number)]

class Hand(Deck):
    def __init__(self, player):
        self.cards = []
        self.player = player
    def pickup(self, card):
        self.cards.append(card)
    def discard(self):
        return self.cards.pop(0)
    
class Game:
    def __init__(self):
        players = []
        num_players = int(input("How many players?: "))
        if num_players < 2:
            raise RuntimeError("You must have at least two players!")
        if num_players > 52:
            raise RuntimeError("You must have 52 or fewer players!")
        self.num_players = num_players
        self.deck = Deck()
        players.append(input("Enter player: "))
        for i in range(1, num_players):
            players.append(input("Enter next player: "))
        self.players = players
        self.hands = [Hand(player) for player in players]
        self.play_game()
        
    def play_game(self):
        print("Shuffling...")
        time.sleep(2)
        self.deck.shuffle()
        
        print("Dealing...")
        time.sleep(2)
        self.deck.deal(self.hands, len(self.deck.cards))
        for hand in self.hands:
            if len(hand.cards) > min([len(hand.cards) for hand in self.hands]):
                hand.discard()
        self.print_hands()

        while [hand.is_empty() for hand in self.hands].count(False) > 1:
            self.battle()
            self.print_hands()
            for hand in self.hands:
                if hand.is_empty():
                    self.remove_hand(hand)
                    self.num_players -= 1

        for hand in self.hands:
            if not hand.is_empty():
                print("{} wins the game!".format(hand.player))
                return
        
    def print_hands(self):
        for hand in self.hands:
            if hand.is_empty():
                s = hand.player + " has no cards."
            else:
                s = hand.player + " has " + str(len(hand.cards)) + " cards."
            print(s)
        print("\n")
        time.sleep(2)

    def remove_hand(self, hand):
        del self.hands[self.hands.index(hand)]
        del self.players[self.players.index(hand.player)]
    
    def battle(self):
        print("Battle!\n")
        time.sleep(2)
        played_cards = []
        for i in range(self.num_players):
            played_cards.append(self.hands[i].discard())
            print("{} played a {}".format(self.players[i], played_cards[i]))
        print("\n")
        time.sleep(2)
        winners = []
        for i in range(len(played_cards)):
            if played_cards[i] == max(played_cards):
                winners.append(self.hands[i])
        if len(winners) == 1:
            print("{} wins the battle!\n".format(winners[0].player))
            for card in played_cards:
                winners[0].pickup(card)
        elif len(winners) > 1:
            war_winner, war_winnings = self.war(winners)
            played_cards += war_winnings
            for card in played_cards:
                war_winner.pickup(card)

    def war(self, winners):
        print("War!\n")
        time.sleep(2)
        print("Players will discard one card each prior to the war...\n")
        discards = []
        war_cards = []
        for winner in winners:
            discards.append(winner.discard())
            war_cards.append(winner.discard())
        time.sleep(2)
        for i in range(len(winners)):
            print("{} played a {}".format(winners[i].player, war_cards[i]))
        time.sleep(2)
        print("\n")
        war_winners = []
        for i in range(len(war_cards)):
            if war_cards[i] == max(war_cards):
                war_winners.append(winners[i])
        if len(war_winners) == 1:
            print("{} wins the war!\n".format(war_winners[0].player))
            return (war_winners[0], discards + war_cards)
        elif len(war_winners) > 1:
            return self.war(war_winners)

        
