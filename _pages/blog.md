---
layout: default
title: blog
permalink: /blog/
---

<div class="default-width">
  <h1>Blog</h1>
  <!-- <p>Posts about puzzles, art, and whatever else I'm building.</p> -->

  <ul class="post-list">
    {% for post in site.posts %}
    <li class="post-list-item">
      <span class="post-list-date">{{ post.date | date: "%d %b, %Y" }}</span>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endfor %}
  </ul>
</div>
