---
layout: index
title: "A mind for language"
subtitle: Fletcher Hardison
---

Posts by Fletcher Hardison on Ancient Greek, language learning, Python, and memory stuff.

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