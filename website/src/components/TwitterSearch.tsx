import React, {useState} from 'react';
import {InputBase} from '@mui/material';
import {Typography} from '@mui/material';
import './SearchBar.css'
interface SearchBarProp{fetchData: (subreddit : string) => void}

const TwitterSearch = ({fetchData}:SearchBarProp) =>{
    const [query,setQuery] = useState('')
    return(
    <div className='searchbar'>
       <div className = 'search-container'>
        <label htmlFor="header-search">
            <span className="visually-hidden"></span>
        </label>
        <div className= 'search'>
            <input
                value={query}
                onChange={(e)=>{setQuery(e.target.value)}}
                type="text"
                id="header-search"
                placeholder="Search twitter keywords"
                name="s" 
            />
        </div>
        <div className= 'button3'>
            <button onClick={()=>(fetchData(query))} type="submit">Search</button>
        </div>
        </div>
    </div>
)};

export default TwitterSearch