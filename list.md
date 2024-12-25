---
layout: default
---

<style>
a.todo { color:red; }
a.doing { color:green; }
</style>

{% assign alldocs = site.documents %}

<div class="container">
  <div class="notes">
    <h1> Everything</h1>
    {%- for document in alldocs -%}
      <div style="display:flex">
        <div style="flex: 0 0 480px;">
          <a href="{{ site.url }}{{ document.url }}" class="{{ document.status }}">
            {{ document.title }}
          </a>
        </div>
        <div style="flex: 0 0 100px;">
          {%- for tag in document.tags -%}
            {{tag}}
          {% endfor%}
        </div>
      </div>
    {% endfor %}
  </div>
</div>