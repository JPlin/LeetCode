# prefix and suffix search
class WordFilter:

    def __init__(self , words):
        '''
        :type words: List[str]
        '''
        self.words = words
        # brute force
        self.map = {}
        for idx , word in enumerate(words):
            for x in range(len(word) + 1):
                prefix = word[:x]
                for y in range(len(word) + 1):
                    suffix = word[y:]
                    self.map[prefix + '#' + suffix] = idx

    def f(self , prefix , suffix):
        '''
        :type prefix: str
        :type suffix: str
        :return type: int
        '''
        return self.map.get(prefix + '#' + suffix , -1)