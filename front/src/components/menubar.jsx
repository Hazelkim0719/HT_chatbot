import React, {useState} from 'react'
import "./menubar.css";

function MenuBar() {
  
  const notice = [ 
    "🚨 뉴스는 8시 ~ 21시 사이에 1시간 30분 간격으로 업데이트 됩니다. 🚨",
    "⚡️ 카카오톡 알람 서비스의 메세지 개수가 9개에서 5개로 변경되었습니다. ⚡️"
  ]

  return(
      <div className="content-top">
        <div className="content-heading">AI 요약 뉴스</div>
        <div className="notice-container">
          <div className="notice-text-wrapper">
            {notice.map((item) => (
              <div className="notice-text">{item}</div>
            ))}
          </div>
        </div>
      </div>
  )
    
}

export default MenuBar
