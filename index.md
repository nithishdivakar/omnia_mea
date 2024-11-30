---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

<style>
a.todo { color:red; }
a.doing { color:green; }
.container{
    display: grid;
    grid-template-areas: 
    "middle right";
    grid-template-columns: 600px 300px;
    column-gap:20px;
}
.notes {
    grid-area: middle;
    height: 95vh;
    overflow: scroll;
}
.toc {
    grid-area: right;
    overflow: scroll;
    height: 95vh;
}
.note{
    margin-bottom: 25px;
}

</style>
<div class="container">
    <div class="notes">
    {% for note in site.notes %}
        <!-- <br><br>
        {{ note.name }} -->
        <!-- <br> -->
        <div id="{{ note.index }}" class="note">
        {{ note.content }}
        </div>  
    {% endfor %}
    </div>
    <div class="toc">
    <b>Table of Contents</b>
        <ul style="font-family:monospace">
        {% for note in site.notes %}
            <li>
                <a href="#{{ note.index }}" class="{{ note.status }}">{{ note.title }}</a>
            </li>
        {% endfor %}
        </ul>
    </div>
</div>