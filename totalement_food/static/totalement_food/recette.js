window.addEventListener("scroll", () => {
  let scrollValue =
    (window.scrollY + window.innerHeight) / document.body.offsetHeight;

  //photo galette
  if (scrollValue > 0.1) {
    photoGalette.style.opacity = 1;
    photoGalette.style.transform = "none";
  }
});
Footer;
