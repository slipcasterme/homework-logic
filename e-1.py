print("A B C ¬(A & B & C) → (¬B ∨ ¬C)")
for a in [0, 1]:
  for b in [0, 1]:
    for c in [0, 1]:
      print(a, b, c, (not(a and b and c)) <= (not(b) or not(c)))