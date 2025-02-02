from string import Template

template  = Template("""---
date: 2024-01-01 00:00:00 +0000
index: '$id'
layout: post
status: done
title: $id $question
tags: []
---

## $question [LC#NUMBER]
> Question Description

### Intuition

### Code

### Time complexity
$T(n) = $ $S(n) = $
"""
              
)
def main():
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(description='My Program')
    parser.add_argument('-i', '--id', help='id')
    parser.add_argument('-q', '--question', help='id')

    args = parser.parse_args()
    t = template.substitute(id=args.id, question=args.question)
    file_path = Path(f"_lc_notes/{args.id} {args.question}.md")
    if file_path.is_file():
        print("File exists")
    else:
        with open(file_path,"w") as F:
            F.write(t)

if __name__ == '__main__':
    main()