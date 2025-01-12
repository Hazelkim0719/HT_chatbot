import React from 'react'
import "./content.css";
import Annotation from './annotation';
function Content({item}) {

  
  return(
    <div>
      <div className="content-summary">
        <strong>3줄요약</strong>
        <ul>
          {item.abstract.map((item, index) => (
            <li key={index}>
              {item}
            </li> 
          ))}
        </ul>
      </div>
      {item.content}
      <Annotation item={item}/>
      
    </div>
  )
    
}

export default Content
