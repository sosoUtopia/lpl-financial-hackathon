import React from "react";

function Header() {
  return (
    <nav className="navBar">
      <img className="icons" src={require("./logos/profit.png")} alt="logo" />
      <h1>Saidit-Readit</h1>
      <div className="iconsRight">
        <img
          className="iconAlpaca"
          src={require("./logos/alpaca.png")}
          alt="AlpacaLogo"
        />
        <img
          className="icons"
          src={require("./logos/reddit.png")}
          alt="RedditLogo"
        />
      </div>
    </nav>
  );
}

export default Header;
