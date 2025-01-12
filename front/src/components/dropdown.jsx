import React, {useState} from 'react'
import "./dropdown.css";
import Content from './context/content';
import Title from './context/title';
import ContentInfo from './context/contentInfo';

function Summary({data}) {
  const [activeIndex, setActiveIndex] = useState(null);

  
  const handleClick = (index) => {
    setActiveIndex(index === activeIndex ? null : index); // 같은 항목 클릭 시 닫기
  };

  
  return(
    <div className="content-container">
      <h2 className="content-heading">AI 요약 뉴스</h2>
      <ul>
        {data.map((item, index) => (
          <li key={index} className="content-item" onClick={() => handleClick(index)}>
            <Title item={item}/>
            <ContentInfo item={item}/>
            <p className={`content-body ${activeIndex === index ? "active" : ""}`}>
              <Content item={item}/>
            </p>
          </li>
        ))}
      </ul>
    </div>
  )
    
}

export default Summary
