a=[
    {
        "movie":"toxic",
        "year":2026,
        "actor":["yash","kiara","tara","huma"]
    },
    {
        "movie":"awarapan2",
        "year":2026,
        "actor":["himesh","disha"]
    },
    {
        "movie":"batwaara",
        "year":2026,
        "actor":["sunny","aamir","preity","vicky"]
    },
    {
        "movie":"bandar",
        "year":2026,
        "actor":["bobby","sanya"]
    },
    {
        "movie":"chavva",
        "year":2025,
        "actor":["vicky","rashmika"]
    }
]
for i in a:
  print(i['movie'])
for j in a:
  print(j['year'])
search = input("Enter actor name: ")
for n in a:
    if search in n['actor']:
        print(n['movie'])
