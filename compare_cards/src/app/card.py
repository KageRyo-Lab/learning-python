def compare_cards(card1, card2):
    cardList = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    if card1 not in cardList or card2 not in cardList:
        raise ValueError()
    
    if card1 == card2:
        return 'Equal'
    
    return card1 if cardList.index(card1) > cardList.index(card2) else card2