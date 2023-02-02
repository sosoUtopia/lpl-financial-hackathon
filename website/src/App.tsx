import axios from "axios";
import React, { useEffect, useState } from "react";
import "./App.css";
import Card from "./components/Card";
import CardsContainer from "./components/CardsContainer";
import RedditSearch from "./components/RedditSearch";
import Header from "./components/Header";
import TwitterSearch from "./components/TwitterSearch";

function App() {
  //empty object is true!!
  const [data, setData] = useState<any>(0);

  async function fetchData(subreddit: string) {
    let response = await axios.get(
      `http://127.0.0.1:8000/subreddit/comments/${subreddit}?limit=2`
    );
    let data = await response.data;
    setData(data);
  }

  useEffect(() => {
    fetchData("wallstreetbets");
  }, []);

  return (
    <div className="App">
      <Header />
      <RedditSearch fetchData={fetchData}/>
      {/* <TwitterSearch fetchData={fetchData}/> */}
      <CardsContainer>
        {data
          ? data.map((element: any) => (
              <Card
                title={element.title}
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
