def spin_words(sentence):
   my_list = sentence.split()
   result = ''
   for i in range(len(my_list)):
      x = my_list[i]
      if len(x) >= 5:
         x = x[::-1]
      if i != 0:
         result = result + ' ' + x
      else:
         result += x

   return result

s = 'rettel rettel Kata than in etirW than desrever the in gnirts gnirts'


def spin_word_kata(sentence):
   return " ".join([x[::-1] if len(x)>=5 else x for x in sentence.split()])
print(spin_word_kata(s))

my_list = ['hello', 'how', 'are', 'you']
print(' '.join(my_list), end='\n')
print(' '.join([x[::-1] if x != 'you' else x for x in my_list]))