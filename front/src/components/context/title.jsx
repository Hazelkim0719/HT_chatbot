import React, {useState} from 'react'
import "./title.css";
function Title({item}) {
  return(
    <div className="content-title"> 
        {item.title}
    </div>
  )
    
}

export default Title
