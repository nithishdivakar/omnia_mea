import frontmatter
from pathlib import Path
import os

for idx, path in enumerate(Path(".").glob("*.md")):
    # print(path)
    post = frontmatter.load(path)
    if not (path.name.split(" ")[0] == post['index'] == post['title'].split(" ")[0]):
        print(path)

    # print(frontmatter.dumps(post))
    # with open(path,'w') as F:
    #     F.write(frontmatter.dumps(post))



# # ---
# # layout: post
# # title:  "06a05__Binary Tree from its Traversals"
# # date:   2024-01-01 00:00:00 +0000
# # categories: 
# # status: doing
# # ---
  
# # >>> frontmatter.dump(post, f)