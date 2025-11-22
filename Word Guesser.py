import random
word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi', 'yeet', 'ligma', 'bepis', 'sussy', 'amongus', 'noob', 'poggers', 'cheems', 'dank', 'cringe', 'flex', 'vibe', 'clout', 'drip', 'slaps', 'cap', 'uncap', 'simp', 'based', 'fyp', 'glizzy', 'chad', 'woke', 'sus', 'fronk', 'bet', 'fire', 'lit', 'savage', 'meme', 'hype', 'swole', 'yeet', 'dab', 'boomer', 'stan', 'troll', 'vaxxed', 'rekt', 'bussin', 'canceled', 'ghosted', 'jacked', 'lowkey', 'highkey', 'shook', 'slay', 'spill the tea', 'throw shade', 'wya', 'wyd', 'zaddy', 'glow up', 'no cap', 'periodt', 'big yikes', 'fit', 'snatched', 'sksksk', 'and i oop', 'cheugy', 'finna', 'goat', 'mood', 'ok boomer', 'peep', 'rizzed up', 'simping', 'vax', 'whip', 'yeeting', 'betting', 'clapped', 'dripped', 'flexed', 'ghosting', 'jacking', 'slayed', 'trolling', 'vaxxing', 'cancelling', 'shooketh', 'ketuahutan', ]
word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 6
while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessedWord))

  guess = input('Guess a letter: ').lower()

  if guess in word:
    for i in range(len(word)):
        if word[i] == guess:
            guessedWord[i] = guess
    print('Great guess!')
  else:
    attempts -= 1
    print('Wrong guess! Attempts left: ' + str(attempts))
  if '_' not in guessedWord:
    print('\nCongratulations!! You guessed the word: ' + word)
    break

if attempts == 0 and '_' in guessedWord:
  print('\nYou\'ve run out of attempts! The word was: ' + word)

