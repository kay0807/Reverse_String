input = "four score and seven years ago"


reverse_str = ""

for char in range(len(input) - 1, -1, -1):
    reverse_str += input[char]

print reverse_str


