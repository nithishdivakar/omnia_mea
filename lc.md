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
        <h1>Competitive Programming Notes</h1>
        <div class="note">
            [ <span class="todo">   todo: </span> {{ todo_count }}
            | <span class="doing"> doing: </span> {{ doing_count }} 
            | <span class="done">   done: </span> {{ done_count }} 
            | <span class="other"> other: </span> {{ other_count }} 
            ]
        </div>
        
        {% for note in site.lc_notes %}
            <div class="note" id="{{ note.slug }}">
                <div style="text-align: right;height:5px">
                    <a name="{{ note.slug }}"  href="{{ note.url | prepend:site.baseurl}}" class="xxs grey monospace">{{ note.slug }}</a>
                </div>
                
                {{ note.content }}
                {% if note.status=='todo' %}
                    (todo)
                {% endif %}
                {% for tag in note.tags %}
                    <span class="tag"> {{ tag }}</span>
                {% endfor %}
            </div>  
        {% endfor %}
    </div>
   
    <div class="toc">
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