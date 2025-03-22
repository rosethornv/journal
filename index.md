---
layout: default
title: My Journal Blog
---

# Welcome to My Journal Blog

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }}) ({{ post.date | date: "%B %d, %Y" }})
{% endfor %}
