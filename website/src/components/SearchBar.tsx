import React, {useState} from 'react';
import {InputBase} from '@mui/material';
import {Typography} from '@mui/material';
import './SearchBar.css'

const SearchBar = () =>(
    <div className='searchbar'>
        <form action="/" method="get">
        <label htmlFor="header-search">
            <span className="visually-hidden"></span>
        </label>
        <div className= 'search'>
            <input
                type="text"
                id="header-search"
                placeholder="Search subreddits"
                name="s" 
            />
        </div>
        <div className= 'button3'>
            <button type="submit">Search</button>
        </div>
        
        </form>
    </div>
    
);

export default SearchBar;