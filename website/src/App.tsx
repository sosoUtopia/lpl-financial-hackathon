import axios from "axios";
import React, { useEffect, useState } from "react";
import "./App.css";
import Card from "./components/Card";
import CardsContainer from "./components/CardsContainer";
import SearchBar from "./components/SearchBar";
import Header from "./components/Header";

function App() {
  //empty object is true!!
  const [data, setData] = useState<any>(0);

  async function fetchData(subreddit: string) {
    let response = await axios.get(
      `http://127.0.0.1:8000/subreddit/comments/${subreddit}?limit=3`
    );
    let data = await response.data;
    setData(data);
  }

  useEffect(() => {
    fetchData("wallstreetbets");
  }, []);

  useEffect(() => {
    console.log(data);
  }, [data]);

  return (
    <div className="App">
      <Header />
      <SearchBar/>
      <CardsContainer>
        {data
          ? data.map((element: any) => (
              <Card
                comment={element.comment}
                sentiment={element.sentiment}
                symbol={element.symbol}
              />
            ))
          : "loading.."}
      </CardsContainer>
    </div>
  );
}

export default App;
