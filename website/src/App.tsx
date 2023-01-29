import React from 'react';
import SearchBar from './components/SearchBar';
import { useState } from 'react'
import './App.css';
// const posts = [
//   {id: '1', name: 'apple'},
//   {id: '2', name: 'bananna'},
//   {id: '3', name: 'test3'},
// ];
// const { search } = window.location;
// const query = new URLSearchParams(search).get('s');


// const filterPosts = (posts: any, query: any) =>{
//   if(!query){
//     return posts;
//   }
//   return posts.filter((post: any) => {
//     const postName = post.name.toLowerCase();
//     return postName.includes(query);
//   });
// };
// const [searchQuery, setSearchQuery] = useState(query || '');
// const filteredPosts = filterPosts(posts, query);
function App() {
  return (
    <div className="App">
      Hello
      <SearchBar
          // searchQuery={searchQuery}
          // setSearchQuery={setSearchQuery}
      />
      {/* <ul>
          {filteredPosts.map((post: any) => (
            <li key={post.id}>{postMessage.name}</li>))}
          
      </ul> */}
    </div>
  );
}

export default App;
