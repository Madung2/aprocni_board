def has_numbers(inputs:str)->bool:
    """
    인자로 받은 문자열에 숫자가 있는지 확인하는 함수
    """
    return any(char.isdigit() for char in inputs)


def has_negative_words(request):
    BAD_WORDS=["바보", "멍청이", "나쁜말1", "나쁜말2"]
    if BAD_WORDS in request.data['comment']:
        return True
    return False
