---
layout: default
---

{% assign alldocs = site.documents | where_exp: 'doc', 'doc.tags.size > 0' %}
{% assign grouptag = alldocs | map: 'tags' | flatten | uniq | sort %}

<div class="container">
    <div class="toc">
        <h1>Collections</h1>
        <ul>
            {% for collection in site.collections %}
                <li>
                    <a href="{{ collection.root_url }}">{{ collection.long_name }}</a>
                </li>
            {% endfor %}
        </ul>
    </div>
    <div class="notes">
        <h1>Tags</h1>
        {%- for tag in grouptag -%}
            <h2>{{- tag -}}</h2> 
            <!-- {{- alldocs | where: 'tags', tag | size -}}</h2> -->
            <ul>
            {%- for document in alldocs -%}
                {% if document.tags and document.tags contains tag %}
                    <li><a href="{{document.url}}">{{- document.title -}}</a></li> 
                {% endif %}
            {%- endfor -%}
            </ul>
        {%- endfor -%}
    </div>
</div>