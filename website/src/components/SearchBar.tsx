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
        <input
            type="text"
            id="header-search"
            placeholder="Search subreddits"
            name="s" 
        />
        <button type="submit">Search</button>
        </form>
    </div>
    
);

export default SearchBar;