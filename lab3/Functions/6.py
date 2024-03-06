def reverse(s):
    words = []
    words = s.split(" ")
    reverse = words[::-1]
    reverse_sentence = " ".join(reverse)
    return reverse_sentence

sanzhar = input()
rev = reverse(sanzhar)
print(rev)
