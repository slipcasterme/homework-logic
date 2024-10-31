print("A B C (𝐴 ∨ 𝐵) (𝐴 ∨ 𝐵 → C)")
for a in [0, 1]:
  for b in [0, 1]:
    for c in [0, 1]:
      print(f"{a} {b} {c} {a or b:>4} {(a or b) <= c:>9}")
