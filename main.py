# Check if two words are anagrams
def find_anagrams(word, anagram):
  if(sorted(word)== sorted(anagram)):
    return True
  else:
    return False
# Example 
find_anagrams("hello", "check")
