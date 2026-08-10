const illustrationTiles = document.querySelectorAll(".illustrations-tile");
const viewer = document.querySelector(".art-viewer");
const viewerImage = document.querySelector(".viewer-image");
const viewerTitle = document.querySelector(".viewer-title");
const viewerClose = document.querySelector(".viewer-close");
const illustrationData = window.illustrationData || [];

function getIllustration(slug) {
  return illustrationData.find((item) => item.slug === slug);
}

function showViewer(item) {
  if (!item) return;
  viewerImage.src = item.image;
  viewerImage.alt = item.title;
  viewerTitle.textContent = item.title;
  viewer.hidden = false;
  viewer.classList.add("open");
}

function closeViewer(updateHash = true) {
  viewer.hidden = true;
  viewer.classList.remove("open");
  if (updateHash) {
    history.replaceState(null, "", window.location.pathname + window.location.search);
  }
}

function syncViewerFromHash() {
  const slug = window.location.hash.slice(1);
  const item = getIllustration(slug);
  if (item) {
    showViewer(item);
    return;
  }
  closeViewer(false);
}

illustrationTiles.forEach((tile) => {
  tile.addEventListener("click", (event) => {
    event.preventDefault();
    const slug = tile.dataset.slug;
    const item = getIllustration(slug);
    if (!item) return;
    history.replaceState(null, "", `#${slug}`);
    showViewer(item);
  });
});

viewerClose.addEventListener("click", () => closeViewer());
window.addEventListener("hashchange", syncViewerFromHash);
document.addEventListener("DOMContentLoaded", syncViewerFromHash);
