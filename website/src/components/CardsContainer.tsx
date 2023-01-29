<<<<<<< HEAD
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

=======
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

>>>>>>> 64f1b3764f052171076e4a2f398a915bbc75a28a
export default CardsContainer;