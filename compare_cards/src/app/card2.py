def compare_cards(card1, card2):
    card_dict = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8, 'J':9, 'Q':10, 'K':11, 'A':12}

    if card1 not in card_dict or card2 not in card_dict:
        raise ValueError()
    
    if card1 == card2:
        return 'Equal'
    
    return card1 if card_dict[card1] > card_dict[card2] else card2