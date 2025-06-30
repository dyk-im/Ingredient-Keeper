import os
os.environ["OPENAI_API_KEY"] = ""
os.environ["AZURE_OPENAI_ENDPOINT"] = ""
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-05-15"

import requests

# Azure Computer Vision API 설정
SUBSCRIPTION_KEY = ""
ENDPOINT = ""

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import AzureChatOpenAI

def read_image_ocr(image_path):
    """이미지를 Azure OCR API에 전송하고 결과 JSON을 반환합니다."""
    ocr_url = ENDPOINT + "vision/v3.2/ocr"
    headers = {
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
        'Content-Type': 'application/octet-stream'
    }
    try:
        with open(image_path, 'rb') as image:
            image_data = image.read()
    except Exception as e:
        return f" 이미지 읽기 오류: {e}"

    response = requests.post(ocr_url, headers=headers, data=image_data)
    if response.status_code != 200:
        return f" OCR 요청 실패: {response.status_code}, {response.text}"

    return response.json()

def extract_ocr_text(ocr_result):
    """OCR JSON 결과에서 텍스트만 추출하여 문자열로 반환합니다."""
    text = ""
    for region in ocr_result.get("regions", []):
        for line in region.get("lines", []):
            line_text = " ".join(word.get("text", "") for word in line.get("words", []))
            text += line_text + "\n"
    return text.strip()

# 이미지 업로드 셀
image_path = input("이미지의 경로를 입력하세요: ")

ocr_result = read_image_ocr(image_path)
if not isinstance(ocr_result, dict):
  print(ocr_result)

extracted_text = extract_ocr_text(ocr_result)
print("\n 추출된 텍스트:\n")
print(extracted_text)


# 모델 설정
llm = AzureChatOpenAI(model_name="gpt-4o-mini", temperature=0.1)

# 프롬프트 템플릿 설정
chat_prompt = ChatPromptTemplate.from_template(
    "내가 못먹는 재료는 {inputA}인데 {topic} 이중에 내가 못먹는 재료가 포함되어있으면 알려줘"
)

# 사용자 입력 받기
inputA = input("못 먹는 재료들을 쉼표로 입력하세요 (예: 계란, 우유): ")
topic = extracted_text

# 프롬프트 완성
prompt_value = chat_prompt.format_prompt(inputA=inputA, topic=topic)

# 모델에게 질문 보내기
response = llm.invoke(prompt_value)

# 첫 결과 저장
previous_result = response.content

# 결과 출력
print("\n 결과:")
print(previous_result)


# 프롬프트 템플릿 수정: 이전 결과를 포함한 사용자 질문 대응
followup_prompt = ChatPromptTemplate.from_template(
    "이전 대화 내용은 다음과 같습니다:\n\n{previous}\n\n사용자 질문: {question}\n답변:"
)

# 입력값으로 프롬프트 구성
user_input = input("\n💬 무엇이 궁금한가요? ")

prompt_value = followup_prompt.format_prompt(
    previous=previous_result,
    question=user_input
)
# LLM에 요청
response = llm.invoke(prompt_value)

# 결과 출력

print("\n 이어지는 답변:")
print(response.content)

