window.addEventListener("scroll", () => {
  let scrollValue =
    (window.scrollY + window.innerHeight) / document.body.offsetHeight;

  //photo galette
  if (scrollValue > 0.1) {
    photoRecette.style.opacity = 1;
    photoRecette.style.transform = "none";
  }
});
Footer;
