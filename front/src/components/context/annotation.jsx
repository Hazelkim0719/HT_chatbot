import React from 'react'
import "./annotation.css";
import ReadMore from './readmore';
function Annotation({item}) {

  
  return(
    <div className="content-annotation">
        <strong>참고:</strong>
        <ul>
          {item.anntation.map((item, index) => (
                <li key={index}>
                    {item}
                </li>
            ))}
        </ul>
        <ReadMore item={item}/>
    </div>
  )
    
}

export default Annotation
