# 🧾 Ingredient-Keeper

**Azure Workshop - 여행 식품 안전 지킴이**

> 해외에서 식품 라벨을 이해하지 못해 불안했던 경험이 있나요?  
> **Ingredient-Keeper**는 영어 식품 라벨을 스캔해, 못 먹는 재료가 포함되어 있는지를 자동으로 분석해주는 프로젝트입니다.

---

## 🛠 사용 기술 스택

- **Azure Computer Vision OCR**  
  이미지에서 성분 텍스트 자동 추출

- **Azure OpenAI (GPT)**  
  사용자의 알러지 정보와 OCR 결과 비교 및 의미 분석

- **Azure App Service / Instance**  
  애플리케이션 배포 및 실행 환경

- **Python**  
  전체 로직 구성 및 API 처리

---

## ⚙️ 동작 원리

1. **이미지 업로드**  
   사용자는 영어로 된 식품 라벨 이미지를 업로드합니다.

2. **OCR 분석**  
   Azure Computer Vision을 통해 이미지에서 성분 텍스트를 추출합니다.

3. **GPT 분석**  
   사용자가 입력한 알러지/기피 재료 목록과 OCR 결과를 비교해 포함 여부를 판단합니다.

4. **자연어 질의 응답 지원**  
   분석 후, 사용자는 LLM과의 자유 대화를 통해 예를 들어  
   “이 제품에 유제품이 포함되었나요?” 같은 추가 질문도 할 수 있습니다.

---

## 📸 예시

| 라벨 이미지 업로드 | 결과 분석 화면 |
|-------------------|----------------|
| ![OCR 예시 1](https://github.com/user-attachments/assets/a4f669fe-ee01-4073-9671-ead1a3de1c34) | ![분석 결과 예시 2](https://github.com/user-attachments/assets/10c8c84d-9125-4998-a2c6-472bd894e114) |

> 위 예시는 영어 식품 라벨에서 OCR을 통해 성분을 추출하고, 사용자의 알러지 정보를 기반으로 GPT가 위험 성분을 분석한 결과입니다.


