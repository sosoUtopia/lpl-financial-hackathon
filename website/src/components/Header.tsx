import React, {useState} from "react";

function Header() {
  return (
    <nav className="navBar">
      <img className="icons" src={require("./logos/profit.png")} alt="logo" />
      <h1>Saidit-Readit</h1>
      <div className="iconsRight">
        <a href="https://app.alpaca.markets/" target={'_blank'}>
          <img 
            
            className="iconAlpaca"
            src={require("./logos/alpaca.png")}
            alt="AlpacaLogo"
          />
        </a>
        <a href="https://www.reddit.com/" target={'_blank'}>
          <img
            className="icons"
            src={require("./logos/reddit.png")}
            alt="RedditLogo"
          />
        </a>
      </div>
    </nav>
  );
}

export default Header;
