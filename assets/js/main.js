const root=document.documentElement;
const nav=document.querySelector(".site-nav");
const navToggle=document.querySelector(".nav-toggle");
const themeToggle=document.querySelector("#theme-toggle");

const saved=localStorage.getItem("theme");
if(saved) root.dataset.theme=saved;
else if(window.matchMedia("(prefers-color-scheme: dark)").matches) root.dataset.theme="dark";

navToggle.onclick=()=>nav.classList.toggle("open");

themeToggle.onclick=()=>{
  root.dataset.theme=root.dataset.theme==="dark"?"light":"dark";
  localStorage.setItem("theme",root.dataset.theme);
};