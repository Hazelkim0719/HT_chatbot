import React from 'react'
import "./readmore.css";
function ReadMore({item}) {
  return(
    <a className="read-more-button"
        href={item.url} 
        target="_blank" 
        rel="noopener noreferrer">
      <button>기사 보기</button>
    </a>
  )
    
}

export default ReadMore
