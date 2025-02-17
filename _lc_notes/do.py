import frontmatter
from pathlib import Path
import os

for idx, path in enumerate(sorted(Path(".").glob("*.md"), reverse=True)):
    # print(path)
    post = frontmatter.load(path)
    if path.name.split(" ")[0]!= post['slug']:
      print(path)
      post['slug'] = path.name.split(" ")[0]
      with open(path,'w') as F:
        F.write(frontmatter.dumps(post))
    if len(post['slug'])==2:
      if 'level' not in post or post['level']!= 'h1':
        print(">",path)

#     FROM="7501"
#     TO="75a"
#     if post['slug'][:len(FROM)]==FROM:
#       post['slug'] = TO + post['slug'][len(FROM):]
        
# #     # if not (path.name.split(" ")[0] == post['index'] == post['title'].split(" ")[0]):
# #     #     print(path)
# #     # del post["index"]
#       should_be_path = f"{post['slug']} {post['title']}.md"
#       if str(path) != should_be_path:
#           print(f"""mv "{path}" "{should_be_path}" """)

#     # print(frontmatter.dumps(post))
#     # with open(path,'w') as F:
#     #     F.write(frontmatter.dumps(post))



# # # ---
# # # layout: post
# # # title:  "06a05__Binary Tree from its Traversals"
# # # date:   2024-01-01 00:00:00 +0000
# # # categories: 
# # # status: doing
# # # ---
  
# # # >>> frontmatter.dump(post, f)

