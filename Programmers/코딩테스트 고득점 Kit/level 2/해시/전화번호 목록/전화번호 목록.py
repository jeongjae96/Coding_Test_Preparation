def solution(phone_book):
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] in phone_book[j]:
                return False
    
    return True