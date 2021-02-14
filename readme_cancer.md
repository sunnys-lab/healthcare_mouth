# 102021 구강계질환 의료영상 AI 경진대회

`poster`

## 1. 개요

* 구강 내시경 사진 내 악성 병변 존재 여부 탐지

![](https://raw.githubusercontent.com/mnc-challenge/healthcare_mouth/main/img/%EA%B5%AC%EA%B0%95_01.png)

## 2. 데이터 상세

### 데이터 셋 별 이미지 수량

| 데이터 셋    | 건수  | 비율(%) |
| ------------ | ----- | ------- |
| Train        | 4,457 | 80.0    |
| Test_public  | 558   | 10.0    |
| Test_private | 559   | 10.0    |
| 합계         | 5,574 | 100     |

* public / private 구분 기준 비공개

### class 

* 라벨링 규칙
  * 라벨은 악성(Cancer, C) 양성(Benign, B), 정상(Normal, N)으로 파일명에 표기
  * 참가자가 직접 악성과 비악성으로 이진화하여 모델 개발에 사용 (암=1, 양성&정상=0)
* 이미지 파일명 규칙
* 환자ID: 기관코드(A-F) + 기관별 환자번호
* 해부학적 부위: 촬영 부위의 해부학적 위치 
  * T: Tongue, P: Palate, B: Buccal mucosa, O: Others
* **진단라벨**: N: Normal / B: Benign / C: Cancer 
  * A5_28_P_N.jpg, F2_5437_T_C.jpg.
  * 단, 테스트셋은 F2_5438_X_X.jpg

### Label

* 제출 파일 양식(csv)
* pred 열에는 암(1)에 대한 예측 확률 값(predicted proba)으로 작성

```
filename,pred
A1_1_X_X.jpg,0.065604867
A1_8_X_X.jpg,0.937117042
```
