c = "MtMdDsFmMdHsMdMdUuo"
atoms = { "Mt": 109, "Md": 101, "Ds": 110, "Fm": 100, "Hs": 108, "Uuo": 118}
for key, value in atoms.items():
    c = c.replace(key,chr(value))
print(c)
