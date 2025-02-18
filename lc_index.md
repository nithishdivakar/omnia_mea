---
layout: default
---

<div class="container">
    <div class="notes">
        <h3> Table of Contents </h3>
        <ul style="font-size: smaller;">
        {% for note in site.lc_notes %}
            <li>
                <a href="{{ note.url | prepend:site.baseurl}}" class="{{ note.status }}{% if note.level %} {{ note.level }}{% endif %}">{{note.slug}} {{ note.title }}</a>
                <br>
                {% if note.tags.size > 0 %}
                <ul><li><span style="font-size: x-small;color: green;">[
                {% for tag in note.tags %}
                    {% if forloop.index0 != 0 %} | {% endif %}
                    {{ tag }}
                {% endfor %}
                ]</span></li></ul>
                {% endif %}
            </li>
        {% endfor %}
        </ul>
    </div>
</div>