class ParserUtils:

    @staticmethod
    def get_values_beetween(message:str, start_pivot:str, end_pivot:str):

        start_pivot_index = message.find(start_pivot)

        if start_pivot_index == -1:
            return None
        
        start_pivot_index += len(start_pivot)
        
        end_pivot_index = message.find(end_pivot)

        values_beetween = message[start_pivot_index:end_pivot_index]

        return values_beetween

    @classmethod
    def try_to_find_keyword(cls, message, start_index:int, keyword_to_check:str) -> int:
        '''
            Returns the index of the first keyword informed in the keyword_to_check parameter found on the message.
        '''

        return message.find(start_index, keyword_to_check)
    
    @classmethod
    def try_to_find_keywords(cls, message, start_index:int, keywords_to_check:str) -> list[tuple]:

        keywords_found = []

        for keyword in keywords_to_check:
            idx = cls.try_to_find_keyword(message, start_index, keyword)
            
            if idx > 0:
                keywords_found.append((keyword, idx))

        return keywords_found

        
