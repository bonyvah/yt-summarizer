from gilas import plist

a = "https://www.youtube.com/watch?v=wTT8QaE0nnw&t=2s"
b ="https://youtu.be/wTT8QaE0nnw?si=9nWDXr4T-1R7UUNE"

if "youtube" in a: 
  print(a[a.index("=")+1:a.index("&t")])
if "youtu.be" in b:
  print(b[b.index(".be/") + 4:b.index("?si")])
