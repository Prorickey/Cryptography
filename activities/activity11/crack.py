f = open("text", "r")
text = f.read()

n = 3
p = 22

print(((17 * n) - p) % 26)

plaintext = ""
for l in text:
	if l == 'S':
		plaintext += 'e'
	elif l == 'R':
		plaintext += "t"
	elif l == 'X':
		plaintext += "h"

	elif l == 'A':
		plaintext += "o"
	elif l == 'Y':
		plaintext += "s"
	elif l == 'U':
		plaintext += "a"
	else:
		plaintext += l

print(plaintext[0:1000])