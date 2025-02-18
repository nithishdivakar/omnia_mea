---
layout: default
---


{% assign todo_count = 0 %}
{% assign doing_count = 0 %}
{% assign done_count = 0 %}
{% assign other_count = 0 %}

{% for note in site.lc_notes %}
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
        <h3> Table of Contents </h3>
        <ul style="font-size: smaller;">
        {% for note in site.lc_notes %}
            <li>
                <a href="#{{ note.slug }}" class="{{ note.status }}{% if note.level %} {{ note.level }}{% endif %}">{{note.slug}} {{ note.title }}</a>
            </li>
        {% endfor %}
        </ul>
    </div>
</div>