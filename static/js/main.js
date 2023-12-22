function showNavbar(color1, color2 ,color3 ,color4 ) {
  document.write(`
    <!--         Nav_Bar         -->
    <div class="header" id="fixed">
      <div class="logo">
        <img src="/static/pics/logo.png" alt="error" />
        <p>BUS FINDER</p>
      </div>
      <div class="right-side">
        <div class="navbar">
          <ul>
            <li>
              <a href="home" style="color:#${color1}">HOME</a>
            </li>
          </ul>
          <ul>
            <li>
              <a href="about" style="color:#${color2}">ABOUT</a>
            </li>
          </ul>
          <ul>
            <li>
              <a href="add" id="services" style="color:#${color3}">ADD</a>
            </li>
          </ul>
          <ul>
            <li>
              <a href="footer" style="color:#${color4}">CONTACT US</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <!--         Nav_Bar         -->
        `);
}

window.addEventListener("load", () => {
  const loader = document.querySelector(".loader");
  loader.classList.add("loader-hidden");
  // loader.addEventListener("transitionend", () => {
  //   document.body.removeChild("loader");
  // });
});
