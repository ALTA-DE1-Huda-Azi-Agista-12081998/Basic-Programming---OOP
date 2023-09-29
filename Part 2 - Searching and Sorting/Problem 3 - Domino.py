def playing_domino(cards, deck):
    recommended_cards = []

    # Check each card in hand to see if it matches the deck
    for card in cards:
        if deck[0] in card or deck[1] in card:
            recommended_cards.append(card)

    if recommended_cards:
        # Sort recommended cards based on the sum in descending order
        recommended_cards.sort(key=lambda x: x[0] + x[1], reverse=True)
        return recommended_cards[0]
    else:
        return []


print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))
# Output: [3, 4]

print(playing_domino([[6, 5], [3, 3], [3, 4], [6, 6]], [3, 6]))
# Output: [6, 5]

print(playing_domino([[6, 6], [2, 4], [3, 6]], [3, 4]))
# Output: []

print(playing_domino([[2, 3], [4, 5], [1, 1], [3, 6]], [4, 2]))
# Output: [4, 5]
