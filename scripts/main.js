const menuToggle = document.querySelector(".menu-toggle");
const siteNav = document.querySelector(".site-nav");
const navLinks = document.querySelectorAll(".site-nav a");
const yearSlot = document.querySelector("#copyright-year");

if (yearSlot) {
  yearSlot.textContent = String(new Date().getFullYear());
}

if (menuToggle && siteNav) {
  const closeMenu = () => {
    menuToggle.setAttribute("aria-expanded", "false");
    siteNav.classList.remove("is-open");
  };

  menuToggle.addEventListener("click", () => {
    const isOpen = menuToggle.getAttribute("aria-expanded") === "true";
    menuToggle.setAttribute("aria-expanded", String(!isOpen));
    siteNav.classList.toggle("is-open", !isOpen);
  });

  navLinks.forEach((link) => {
    link.addEventListener("click", closeMenu);
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth >= 1024) {
      closeMenu();
    }
  });
}
