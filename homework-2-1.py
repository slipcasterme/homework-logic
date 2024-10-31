print("a | b | c | ¬A ∨ ¬B ∨ C | (A ∨ C) & (¬B ∨ C)")
for a in [0, 1]:
  for b in [0, 1]:
    for c in [0, 1]:
      print(f"{a} | {b} | {c} | {not(a) or not(b) or c:^11} | {(a or c) and (not(b) or c):^17}")