from string import Template

template  = Template("""---
date: 2024-01-01 00:00:00 +0000
slug: '$id'
layout: post
status: done
title: $question
tags: []
---

## $question [LC#$lc]
> Question Description

### Intuition

### Code
```python

```

### Time complexity
- $$T(n) = $$ 
- $$S(n) = $$
"""
              
)
def main():
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(description='My Program')
    parser.add_argument('-i', '--id', help='id')
    parser.add_argument('-q', '--question', help='id')
    parser.add_argument('-l', '--lc', help='id', default="NUMBER")

    args = parser.parse_args()
    t = template.substitute(id=args.id, question=args.question, lc = args.lc)
    file_path = Path(f"_lc_notes/{args.id} {args.question}.md")
    if file_path.is_file():
        print("File exists")
    else:
        with open(file_path,"w") as F:
            F.write(t)

if __name__ == '__main__':
    main()