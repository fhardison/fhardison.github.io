---
layout: index
title: "A mind for language"
subtitle: Fletcher Hardison
---

Learning languages is hard. It requires time,  effort, and above all -- commitment. 

Here you'll find post by me, Fletcher Hardison, on how to learn languages more easily. 

Specially you'll find my thoughts on Ancient Greek, language learning, and memory stuff, oh and the odd bit of Python (yes I'm a nerd). 

## Pages

* [Projects](/projects.html)

{% capture numposts %}{{ site.posts | size }}{% endcapture %}
{% if numposts != '0' %}
## Posts

{% for post in site.posts %}{% assign currentyear = post.date | date: "%Y" %}{% if currentyear != prevyear %}
### {{ currentyear }}
{% assign prevyear = currentyear %}{% endif %} - [{{ post.title }}]({{ site.baseurl }}{{ post.url }}) - {{ post.date | date: '%B %-d' }}
{% endfor %}
{% endif %}
