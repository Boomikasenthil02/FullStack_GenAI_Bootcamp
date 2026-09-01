def analyze_string(text):
    character=len(text)
    vowels=0
    consonants=0
    for ch in text:
      if ch.lower() in "aeiou":
        vowels=vowels+1
      elif ch.isalpha():
        consonants=consonants+1
    return character,vowels,consonants
result=analyze_string("python")
print("Character =",result[0])
print("Vowels =",result[1])
print("consonants =",result[2])

