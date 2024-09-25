from typing import Union

class ParserUtils:

    @staticmethod
    def get_values_beetween(message:str, start_pivot:Union[str, int], end_pivot:Union[str, int]):
        
        if not isinstance(start_pivot, int) and not isinstance(end_pivot, int):
            start_pivot_index = message.find(start_pivot)

            if start_pivot_index == -1:
                return None
            
            start_pivot_index += len(start_pivot)
            
            end_pivot_index = message.find(end_pivot)
        else:
            start_pivot_index = start_pivot
            end_pivot_index = end_pivot

        values_beetween = message[start_pivot_index:end_pivot_index]

        return values_beetween

    @classmethod
    def try_to_find_keyword(cls, message:str, start_index:int, keyword_to_check:str) -> int:
        '''
            Returns the index of the first keyword informed in the keyword_to_check parameter found on the message.
        '''

        return message.find(keyword_to_check, start_index)
    
    @classmethod
    def try_to_find_keywords(cls, message, start_index:int, keywords_to_check:str) -> list[tuple]:

        keywords_found = []

        for keyword in keywords_to_check:
            idx = cls.try_to_find_keyword(message, start_index, keyword)
            
            if idx > 0:
                keywords_found.append((keyword, idx))

        return keywords_found

    def get_value_beetween_parenthesis(self, message:str, parenthesis_pos=1):

        parenthesis_count = 1
        parenthesis_pos -= 1



        start_idx = message.find('(')
        while start_idx >= 0 and parenthesis_pos != 0:
            start_idx = message.find('(', start_idx + 1)
            parenthesis_pos -= 1

        i = 0

        while i < len(message) - 1:
            
            if message[i] == '(':
                parenthesis_count += 1

            if message[i] == ')':
                parenthesis_count -= 1

            if parenthesis_count == 0:
                break

            i += 1
            
        return message[start_idx+1:i]
