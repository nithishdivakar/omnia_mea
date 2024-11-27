from pathlib import Path

for path in Path(".").glob("*.md"):
  print(path.name)
  s =f"""---
layout: post
title:  "{path.name[:-3]}"
date:   2024-01-01 00:00:00 +0000
categories: 
---
"""
  with open(path) as F:
    lines = F.readlines()
  
  with open(path,"w") as F:
    F.write(s)
    F.write("\n\n")
    for line in lines:
      F.write(line)
