# ukrit = str(input().lower()) 
# kaew = str(input().lower())

# if kaew == ukrit:
#     print("Draw")
# elif kaew == "rock" and ukrit == "scissors":
#     print("Dr.Worarat Krathu")
# elif kaew == 'rock' and ukrit == 'paper':
#     print("Mr.Ukrit Ruckcharti")
# elif kaew == 'paper' and ukrit == 'scissors':
#     print("Mr.Ukrit Ruckcharti")
# elif kaew == 'paper' and ukrit == 'rock':
#     print("Dr.Worarat Krathu")
# elif kaew == 'scissors' and ukrit == 'paper':
#     print("Dr.Worarat Krathu")
# elif kaew == 'scissors' and ukrit == 'rock':
#     print("Mr.Ukrit Ruckcharti")

# Using Dictionary
ukrit = input().lower()
kaew = input().lower()

results = {
    ("rock", "scissors"): "Dr.Worarat Krathu",
    ("rock", "paper"): "Mr.Ukrit Ruckcharti",
    ("paper", "rock"): "Dr.Worarat Krathu",
    ("paper", "scissors"): "Mr.Ukrit Ruckcharti",
    ("scissors", "paper"): "Dr.Worarat Krathu",
    ("scissors", "rock"): "Mr.Ukrit Ruckcharti"
}

if kaew == ukrit:
    print("Draw")
else:
    print(results[(kaew, ukrit)])