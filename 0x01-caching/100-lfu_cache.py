#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.frequency = {}  # Dictionary to keep track of frequency of each key

    def put(self, key, item):
        if key is None or item is None:
            return
        
        # If key already exists, update its frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            # If cache is full, discard least frequency used item
            if len(self.cache_data) >= self.MAX_ITEMS:
                least_frequent_keys = [k for k, v in self.frequency.items() if v == min(self.frequency.values())]
                if len(least_frequent_keys) == 1:
                    del self.cache_data[least_frequent_keys[0]]
                    del self.frequency[least_frequent_keys[0]]
                else:
                    # Use LRU algorithm to discard least recently used among least frequency used items
                    lru_key = min(least_frequent_keys, key=lambda k: self.cache_data[k])
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    least_frequent_keys.remove(lru_key)
            self.cache_data[key] = item
            self.frequency[key] = 1

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        # Increment frequency of accessed key
        self.frequency[key] += 1
        return self.cache_data[key]


if __name__ == "__main__":
    my_cache = LFUCache()

    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "OpenAI")

    print(my_cache.get("A"))  # Output: Hello
    print(my_cache.get("B"))  # Output: World
    print(my_cache.get("C"))  # Output: OpenAI

    my_cache.put("D", "GPT")
    my_cache.put("E", "Chatbot")

    print(my_cache.get("D"))  # Output: GPT
    print(my_cache.get("E"))  # Output: Chatbot
    print(my_cache.get("A"))  # Output: Hello (frequency of A increased)

    my_cache.put("F", "2024")

    print(my_cache.get("C"))  # Output: None (C discarded due to LFU and LRU)
    print(my_cache.get("F"))  # Output: 2024
