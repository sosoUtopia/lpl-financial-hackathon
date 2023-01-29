import React, { useState } from "react";
import axios from 'axios'
import "./Card.css";

interface CardProp extends React.HTMLAttributes<HTMLDivElement> {
  symbol: string;
  sentiment: number;
  comment: string;
  title: string
}

const Card = ({ symbol, sentiment, comment, title }: CardProp) => {
  async function buyStock(stock: string, qty: number) {
    let res = await axios.post(`http://127.0.0.1:8000/subreddit/buy/${stock}?qty=${qty}`)
    console.log(res)
  }

  async function sellStock(stock: string, qty: number) {
    let res = await axios.post(`http://127.0.0.1:8000/subreddit/sell/${stock}?qty=${qty}`)
    console.log(res)
  }

  const [buyQTY, setBuyQTY] = useState(0)
  const [sellQTY, setSellQTY] = useState(0)

  return (
    <div className="card-container">
      <h2>{symbol}</h2>
      <h3>Title: {title}</h3>
      <h3>Sentiment: {sentiment}</h3>
      <p>{comment}</p>
      <div className="order-container">
        <div className="order-sub-container">
          <input value={buyQTY} onChange={e=>setBuyQTY(Number(e.target.value))} placeholder="QTY" />
          <button onClick={()=>{ buyStock(symbol, buyQTY)}} id="buyBtn">Buy</button>
        </div>
        <div className="order-sub-container">
          <input value={sellQTY} onChange={e=>setSellQTY(Number(e.target.value))} placeholder="QTY" />
          <button onClick={()=>{ sellStock(symbol, sellQTY)}} id="sellBtn">Sell</button>
        </div>
      </div>
    </div>
  );
};

export default Card;
