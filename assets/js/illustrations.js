const illustrationTiles = document.querySelectorAll(".illustrations-tile");
const viewer = document.querySelector(".art-viewer");
const viewerImage = document.querySelector(".viewer-image");
const viewerTitle = document.querySelector(".viewer-title");
const viewerCaption = document.querySelector(".viewer-caption");
const viewerClose = document.querySelector(".viewer-close");
const viewerPrev = document.querySelector(".viewer-prev");
const viewerNext = document.querySelector(".viewer-next");
const illustrationData = window.illustrationData || [];
let currentIndex = -1;

function getIllustration(slug) {
  return illustrationData.find((item) => item.slug === slug);
}

function getIllustrationIndex(slug) {
  return illustrationData.findIndex((item) => item.slug === slug);
}

function normalizeIndex(index) {
  if (!illustrationData.length) return -1;
  return (index + illustrationData.length) % illustrationData.length;
}

function goToIllustration(index) {
  const normalizedIndex = normalizeIndex(index);
  const item = illustrationData[normalizedIndex];
  if (!item) return;
  history.replaceState(null, "", `#${item.slug}`);
  showViewer(item);
}

function renderImages(sources) {
  viewerImage.innerHTML = "";
  sources.forEach((src) => {
    const img = document.createElement("img");
    img.src = src;
    img.alt = "";
    viewerImage.appendChild(img);
  });
}

function showViewer(item) {
  if (!item) return;
  currentIndex = getIllustrationIndex(item.slug);
  const sources = item.type === "project" ? item.images || [] : [item.image];
  renderImages(sources);
  viewerTitle.textContent = item.title;
  viewerCaption.textContent = item.description || "";
  viewerCaption.hidden = !item.description;
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
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
});

viewerClose.addEventListener("click", () => closeViewer());
viewerPrev.addEventListener("click", () => {
  if (currentIndex < 0) return;
  goToIllustration(currentIndex - 1);
});
viewerNext.addEventListener("click", () => {
  if (currentIndex < 0) return;
  goToIllustration(currentIndex + 1);
});
window.addEventListener("hashchange", syncViewerFromHash);
document.addEventListener("DOMContentLoaded", syncViewerFromHash);
