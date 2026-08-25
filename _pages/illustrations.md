---
layout: default
title: illustrations
permalink: /illustrations/
full_width: true
---

<!-- <div class="default-width">
  <p>Jump to: <a>projects</a> <a>singles</a></p>
</div> -->

<div class="full-width">
<br>
  <div class="art-viewer" hidden>
    <div class="viewer-panel">
      <div class="viewer-rail">
        <div class="viewer-controls">
          <button class="viewer-button viewer-close" type="button" aria-label="Close artwork">×</button>
          <button class="viewer-button viewer-prev" type="button" aria-label="Show previous artwork">‹</button>
          <button class="viewer-button viewer-next" type="button" aria-label="Show next artwork">›</button>
        </div>
        <div class="viewer-meta">
          <h2 class="viewer-title"></h2>
          <p class="viewer-caption" hidden></p>
        </div>
      </div>
      <img class="viewer-image" src="" alt="">
    </div>
  </div>
</div>

<div class="full-width">
  <h1>Projects</h1>
  <!-- this needs to show only json objects with type project -->
  <div class="illustrations-grid">
    todo
  </div>
</div>

<div class="full-width">
  <h1>Individual Illustrations</h1>
  <!-- this needs to show only json objects with type single -->
  <div class="illustrations-grid">
    {% for item in site.data.illustrations %}
    <a class="illustrations-tile" href="#{{ item.slug }}" data-slug="{{ item.slug }}" data-image="{{ item.image }}" data-title="{{ item.title }}" aria-label="Open {{ item.title }}">
      <img src="{{ item.image }}" alt="{{ item.title }}">
      <span class="tile-overlay"></span>
      <span class="tile-label">open</span>
    </a>
    {% endfor %}
  </div>
</div>

<script>window.illustrationData = {{ site.data.illustrations | jsonify }};</script>
<script src="/assets/js/illustrations.js" defer></script>
