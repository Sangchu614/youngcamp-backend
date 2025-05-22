from django.core.exceptions import ValidationError

BAD_WORDS = ['멍청이', '죽어', '바보']  # 원래 금지어로 채우기

def validate_no_profanity(value):
    for bad in BAD_WORDS:
        if bad in value.lower():
            raise ValidationError("부적절한 단어가 포함되어 있습니다.")
