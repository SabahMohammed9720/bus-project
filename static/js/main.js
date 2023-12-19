function showNavbar(){
    document.write( `
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
              <a href="home">HOME</a>
            </li>
          </ul>
          <ul>
            <li>
              <a href="about">ABOUT</a>
            </li>
          </ul>
          <ul>
            <li>
              <a href="add" id="services">ADD</a>
            </li>
          </ul>
          <ul>
            <li>
              <a href="footer">CONTACT US</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <!--         Nav_Bar         -->
        `
    )
}