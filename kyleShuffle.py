
from random import sample
import random
import copy



def shuffleGift( howManyGift ):
    
    assert type( howManyGift ) == int
    if howManyGift == 2:
        return [2,1]
    elif howManyGift == 1:
        return[1]
    gift = [ i for i in range( 1 , howManyGift + 1 ) ] # 將每一個禮物編號
    giftShuffle = sample( gift , howManyGift )
    state = []

    # 檢查有沒有人拿到自己的禮物或是倆倆互換
    for i in range( howManyGift ):
        a = gift[i]
        aTo = giftShuffle[i]
        b = gift[aTo-1]
        bTo = giftShuffle[aTo-1]
        if a == bTo:
            
            return shuffleGift(howManyGift) 
            break

    return giftShuffle

