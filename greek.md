---
layout: page
title: Greek
permalink: /greek/
---

On this page you will find resources related to Classical and Koine Greek. I am teaching a course on Koine Greek Fall 2018 and intend to include course notes and other relevant material here.    

<h2>Latest posts</h2>

<div>&nbsp;</div>

<ul class="post-list">
  {% for post in site.greek reversed %}
<li>

<div>

<h2>
  <a class="post-link" href="{{ post.url | relative_url }}" title="{{ post.title }}">{{ post.title | escape }}</a>
</h2>

<span>{{ post.excerpt | markdownify | truncatewords: 30 }}</span>

</div>
</li>
{% endfor %}
</ul>