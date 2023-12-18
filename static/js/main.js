function showNavbar(){
    document.write( `
    <div class="header" id="fixed">
        <div class="logo">
            <img src="images/logo.png" alt="">
            <p>BUS FINDER</p>
        </div>
        <div class="right-side">
            <div class="navbar">
                <ul>
                    <li>
                        <a href="land.html" id="home">HOME</a>
                    </li>
                </ul>
                <ul>
                    <li>
                        <a href="about.html" id="about">ABOUT</a>
                    </li>
                </ul>
                <ul>
                    <li>
                        <a href="search.html" id="services">SERVICES</a>
                    </li>
                </ul>
                <ul>
                    <li>
                        <a href="footer.html" id="contact">CONTACT US</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
        `
    )
}