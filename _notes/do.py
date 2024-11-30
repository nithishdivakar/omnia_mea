# import frontmatter
# from pathlib import Path

# for idx, path in enumerate(Path(".").glob("*.md")):
#     print(path)
#     post = frontmatter.load(path)
#     cont = post.content.strip()
#     title = " ".join(post['title'].split("__"))
#     index = title.split(" ")[0]
#     just_title = " ".join(title.split(" ")[1:])
#     post['title'] = title
#     post['index'] = index

#     if len(cont)==0:
#         print(post['status'], index, f"{title}" , path, just_title)
#         post.content = f"## {just_title}"

#     print(frontmatter.dumps(post))
#     with open(path,'w') as F:
#         F.write(frontmatter.dumps(post))


# # ---
# # layout: post
# # title:  "06a05__Binary Tree from its Traversals"
# # date:   2024-01-01 00:00:00 +0000
# # categories: 
# # status: doing
# # ---
  
# # >>> frontmatter.dump(post, f)