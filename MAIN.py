"""
交換禮物並且寄送EMAIL通知
"""
import kyleEmail
import kyleShuffle


if __name__ == "__main__":
    
    gList = kyleEmail.guestList('D:/Document/Program Code/Project/Gift Exchange/GuestEmail.txt')
    n = len(gList)
    giftShuffle = kyleShuffle.shuffleGift(n)


    for i in range(n):
        subject = 'Gift Exange Result-這才是真的，剛剛陳伯軒搞事，所以重新發信'
        content =  '''Hi {},

Your gift recipient is {}.
It means that you need to give a present to {}!!

Sincerely,
Python Script'''.format( gList[i].name, gList[giftShuffle[i]-1].name, gList[giftShuffle[i]-1].name )

        toAddr = gList[i].email
        kyleEmail.sendEmail(subject,content,[toAddr])