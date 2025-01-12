import React, {useState} from 'react'
import "./contentInfo.css";
function ContentInfo({item}) {
  return(
    <div className="content-info">
    <span className="content-date">{item.date}</span>
    <span className="content-section">{item.section}</span>
    </div>
  )
    
}

export default ContentInfo
