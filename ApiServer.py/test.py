import re
def parseAnnotation(annotation_text):
    # 숫자와 마침표 뒤의 내용을 찾는 정규 표현식
    pattern = r'(\d+\.)\s*([^0-9]+)'
    
    # 정규식으로 매칭된 결과를 리스트로 반환
    result = re.findall(pattern, annotation_text)
    # 매칭된 부분을 "숫자. 내용" 형식으로 다시 합쳐서 반환
    return [f"{match[0].strip()} {match[1].strip()}" for match in result]
t = '1. 사모펀드(PEF) : 개인이나 기관의 자본을 모아 특정 기업에 투자하는 투자 기구 2. 인수금융 : 기업 인수 시 필요한 자금을 대출받는 것 3. 매각가 : 판매할 때의 가격'
print(parseAnnotation(t))