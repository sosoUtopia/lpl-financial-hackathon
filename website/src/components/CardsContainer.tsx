import React, {HTMLAttributes} from 'react';
import './CardsContainer.css'
import Card from "./Card";

interface CardsContainerProp extends HTMLAttributes<HTMLDivElement>{}

const CardsContainer = ( { children }: CardsContainerProp) => {
    return (
        <div className="cards-container">
            { children }
        </div>
    );
};

export default CardsContainer;