import React, { useState, useEffect } from "react";
import axios from "axios";
import Summary from "./components/dropdown";
import "./App.css";
function App() {
  const [data, setData] = useState([]);

  // API 호출 함수
  const fetchData = async () => {
    try {
      const response = await axios.get("http://192.168.219.187:5000") // 로컬 API URL
      const apiData = response.data.reverse(); // API 응답 데이터
      

      // 데이터 가공
      const formattedData = apiData.map((item) => ({
        title: item.gpt?.gpt_title || "제목 없음",
        date: item.gpt?.gpt_date || "날짜 없음",
        section: item.gpt?.gpt_section || "주제 없음",
        abstract: item.gpt?.gpt_abstract || "요약 없음",
        content: item.gpt?.gpt_content || "본문 없음",
        anntation: item.gpt?.gpt_annotation || "주석 없음",
        url: item.origin?.url || "https://m.naver.com",
      }));
      setData(formattedData);
    } catch (error) {
      console.error("API 호출 중 오류 발생:", error);
    }
  };

   // 컴포넌트 마운트 시 API 호출
   useEffect(() => {
    fetchData();
  }, []);

  return(
    <div>
      {/* Content 컴포넌트에 data를 props로 전달 */}
      <Summary data={data} />
    </div>
  )
    
}

export default App
