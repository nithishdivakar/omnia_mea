---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

{% assign todo_count = 0 %}
{% assign doing_count = 0 %}
{% assign done_count = 0 %}
{% assign other_count = 0 %}

{% for note in site.notes %}
    {% case note.status %}
        {% when 'todo' %}
            {% assign todo_count = todo_count | plus: 1 %}
        {% when 'doing' %}
            {% assign doing_count = doing_count | plus: 1 %}
        {% when 'done' %}
            {% assign done_count = done_count | plus: 1 %}
        {% else %}
            {% assign other_count = other_count | plus: 1 %}
    {% endcase %}
{% endfor %}


<div class="container">
    <div class="notes">
        <div class="note">
            [ todo: {{ todo_count }} | doing: {{ doing_count }} | done: {{ done_count }} | other: {{ other_count }} ]
        </div>
    {% for note in site.notes %}
        <div class="note"  id="{{ note.index }}">
        <a href="#" id="{{ note.index }}"></a>
        <div style="text-align: right;height:5px">
            <a href="#{{ note.index }}" class="xxs grey monospace">{{ note.index }}</a>
        </div>
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