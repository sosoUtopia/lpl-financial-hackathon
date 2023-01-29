import React from "react";
import "./App.css";
import Card from "./components/Card";
import CardsContainer from "./components/CardsContainer";
import SearchBar from "./components/SearchBar";
import Header from "./components/Header";

function App() {
  return (
    <div className="App">
      <Header />
      <SearchBar/>
      <CardsContainer>
        <Card comment="hello" sentiment={1} symbol="AAPL" />
        <Card comment="hello" sentiment={1} symbol="AAPL" />
        <Card comment="hello" sentiment={1} symbol="AAPL" />

        <Card comment="hello" sentiment={1} symbol="AAPL" />
        <Card comment="hello" sentiment={1} symbol="AAPL" />
      </CardsContainer>
    </div>
  );
}

export default App;
