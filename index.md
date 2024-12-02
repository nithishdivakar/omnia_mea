---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

<div class="container">
    <div class="notes">
    {% for note in site.notes %}
        <div class="note"  id="{{ note.index }}">
        <a href="#{{ note.index }}" id="{{ note.index }}"></a>
        {{ note.content }}
        {% if note.status=='todo' %}
            (todo)
        {% endif %}
        </div>  
    {% endfor %}
    </div>
    <div class="toc">
        <h3> Table of Contents </h3>
        <ul style="font-size: smaller;">
        {% for note in site.notes %}
            <li>
                <a href="#{{ note.index }}" class="{{ note.status }}">{{ note.title }}</a>
            </li>
        {% endfor %}
        </ul>
    </div>
</div>