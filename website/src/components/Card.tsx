import React from "react";
import "./Card.css";

interface CardProp extends React.HTMLAttributes<HTMLDivElement> {
  symbol: string;
  sentiment: number;
  comment: string;
}

const Card = ({ symbol, sentiment, comment }: CardProp) => {
  return (
    <div className="card-container">
      <h2>{symbol}</h2>
      <h3>Sentiment: {sentiment}</h3>
      <p>{comment}</p>
      <div className="order-container">
        <div className="order-sub-container">
          <input placeholder="QTY" />
          <button>Buy</button>
        </div>
        <div className="order-sub-container">
          <input placeholder="QTY" />
          <button>Sell</button>
        </div>
      </div>
    </div>
  );
};

export default Card;
