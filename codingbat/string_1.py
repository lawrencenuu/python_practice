#hello_name
def hello_name(name):
  return "Hello " + name + "!"

#make_abba
def make_abba(a, b):
  return a+b+b+a

#make_tags
def make_tags(tag, word):
  element = "<"+tag+">"+word+"</"+tag+">"
  return element


#make_out_word
def make_out_word(out, word):
  element = out[:2]+word+out[-2:]
  return element

#extra_end
def extra_end(str):
  text = str[-2:]*3
  return text

#first_two
def first_two(str):
  text = str[:2]
  return text

#first_half
def first_half(str):
  return str[:((len(str))/2)]


#without_end
def without_end(str):
  return str[1:-1]

#combo_string
def combo_string(a, b):
  if len(a) < len(b):
    return a+b+a
  else:
    return b+a+b


#non_start
def non_start(a, b):
  return a[1:]+b[1:]

#left2
def left2(str):
  if len(str) <=2:
    return str
  else:
    return str[2:]+str[:2]

