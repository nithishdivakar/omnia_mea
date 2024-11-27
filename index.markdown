---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

<style>
a.todo{
    color:red;
}
</style>

<ul style="font-family:monospace">
{% for note in site.notes %}
  <li>
    <a href="{{ site.url }}{{ note.url }}" class="{{ note.status }}">
      {{ note.name }}
    </a>
  </li>
{% endfor %}
</ul>