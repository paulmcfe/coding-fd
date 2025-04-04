score = int(input("What was your score? "))

if score >= 90:
    print(f"Woot, your score was {score}.")
    print("You get an A+")
elif score >= 80:
    print(f"Wow, your score was {score}.")
    print("You get an A.")
elif score >= 70:
    print(f"Not bad, your score was {score}.")
    print("You get an B.")
elif score >= 60:
    print(f"Okay, your score was {score}.")
    print("You get an C.")
elif score >= 50:
    print(f"Hmm, your score was {score}.")
    print("You get an D.")
else:
    print(f"Oh, snap, your score was {score}.")
    print("You get an F.")