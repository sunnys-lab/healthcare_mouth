# 주의 사항(필독)

* 대회 시작 전 아래 주의 사항을 반드시 숙지하시기 바랍니다

[1. 디렉토리 구조 유지](#1. 디렉토리 구조 유지)

[2. 최종 결과물 저장 형식](# 2. 최종 결과물 저장 형식)

[3. 최종 제출 파일](# 3. 최종 제출 파일)

[4. 재현성 검증 및 시드 고정](# 4. 재현성 검증 및 시드 고정)

[5.  추론 결과 제출](# 5. 추론 결과 제출)

## 1. 디렉토리 구조 유지

![](https://raw.githubusercontent.com/mnc-challenge/healthcare_mouth/main/img/directory.png)

```bash
# 디렉토리 구조
\_DATA								: 데이터 폴더
	\_CANCER						: 구강암 데이터 폴더
		\_TRAIN						: 구강암 학습 데이터 폴더
		\_TEST						: 구강암 테스트 데이터 폴더
	\_TEETH							: 치아 데이터 폴더
		* train_label.json			: 치아 학습 라벨 파일
		\_TRAIN						: 치아 학습 데이터 폴더
		\_TEST						: 치아 테스트 데이터 폴더 
\_USER								: 참가자 사용 폴더
	\_USER_WORKSPACE				: 참가자 작업 폴더
		* submit.py					: 결과 제출 스크립트
	\_INFERENCE						: 최종 결과물 폴더
		\_TEETH						: 치아 최종 결과물 폴더(구강암 디렉토리와 구조 동일)
		\_CANCER					: 구강암 최종 결과물 폴더
			* train.sh				: train.py 실행 스크립트(arguments 포함)
			* inference.sh			: inference.py 실행 스크립트(arguments 포함)
			* train.py				: 학습 스크립트
			* infernce.py			: 추론 스크립트
			* readme.txt			: 스크립트 설명 파일
			\_results				: 결과 폴더
				* result.json(csv)	: 결과 파일
			\_src					: train.py, infernece.py 참조 스크립트
			\_weights				: 모델(가중치) 폴더
	\_PACKAGES						: 추가 라이브러리 요청시 패키지 파일 저장 경로
```

* 최초 서버 세팅 시 위와 같은 형태로 디렉토리 구조를 제공합니다
  * 위 디렉토리 구조를 유지하면서 작업 진행해주시기 바랍니다.
* <span style="color:red">**/USER_WORKSPACE, /src, /weights 에서만 하위 디렉토를 만들어 작업하시기 바랍니다.**</span>
* 디렉토리 이슈로 재현성 검증 실패 시 탈락 사유가 될 수 있으니 유의하시기 바랍니다.
* /DATA 는 읽기 권한만 부여합니다.
* /USER 디렉토리는 참가팀 당 100G 씩 할당합니다. 
  * 100G를 넘을 경우 디렉토리 정리 요청을 드릴 수 있습니다.
* 환경 설정 기간 이후 추가 라이브러리 요청 시, 요청하신 패키지 파일을 /PACKAGES 로 업로드 합니다

## 2. 최종 결과물 저장 형식

* 최종 결과물은 INFERENCE/{대회명}/ 디렉토리 구조를 유지하면서 저장해 주시기 바랍니다.

* train.sh , inference.sh

  * train.py, inference.py 에 arguments 를 넣어 수행할 수 있도록 작성하시기 바랍니다.

    ```shell
    # 예시 train.sh
    python3 train.py --data /DATA/TEETH/TRAIN/ --label /DATA/TEETH/train_label.json --model weights/
    
    # 예시 inference.sh
    python3 inference.py --data /DATA/TEETH/TEST/ --result /results/result.json
    ```

  * <span style="color:red">**재현성 검증 시 train.sh, inference.sh 두 파일만 실행합니다**</span>

    * 스크립트 오류, 재현성 검증 실패 시 탈락 사유가 될 수 있으니 작성에 유의하시기 바랍니다.

* train.py, inference.py

  * 학습/추론 코드는 각각<span style="color:red"> **단일 스크립트**</span>에서 수행할 수 있도록 구성하시기 바랍니다.
  * 학습/추론 코드는 반드시 제공된 원본 데이터(/DATA/..)를 참조해야 합니다. 
    * 스크립트 구성 시 전처리 코드를 포함하시기 바랍니다.
  * 학습/추론 코드에서 참조(import)하는 모든 스크립트는 /src 내에 저장하시기 바랍니다.
  * 학습/추론 코드에서 불러오는 모든 가중치 파일은 /weights내에 저장하시기 바랍니다.
  * 최종 제출 파일(csv, json)은 results/ 내에 저장하시기 바랍니다
  
* readme.txt

  * readme.txt  는 아래 사항을 기입해 주시기 바랍니다.
    1. train.py, inference.py  입력 인자 설명
    2. 리더보드 스코어 및 등수
    3. 활용 모델 간략한 설명
    4. 파이썬 라이브러리 가상환경 활성화 방법
    5. 기타

## 3. 최종 제출 파일

* 리더보드 상 점수에 해당하는 파일을 저장하시기 바랍니다.
* 재현성 검증 시 해당 파일과 재학습 후 생성한 제출 파일이 리더보드 점수를 재현할 수 있는지 확인 합니다.

## 4. 재현성 검증 및 시드 고정

* train.sh, inference.sh 파일을 수행해 재현성 검증을 진행합니다.
* 재현성 검증은 아래 항목을 모두 만족해야 통과할 수 있습니다.
  1. 재학습된 모델로(train.sh 로 생성한 모델) 추론한 결과 파일(inference.sh 로 생성)의 채점결과가 리더보드상 점수와 같음
  2. 최종 제출 파일(치아식별-result.json, 구강암분류-result.csv)의 채점 결과가 리더보드상 점수와 같음
  3. 학습 시 외부 데이터를 참조하거나, 테스트 데이터를 활용하지 않았음
  4. 데이터 유출 등 기타 부정행위 소지가 없음
* 시드 고정을 하지 않으면 재학습 할 때 마다 다른 모델이 생성될 수 있습니다. 
  * pytorch, tensorflow 시드 고정 코드를 참고 바랍니다.
  * 환경에 따라 시드 고정에 실패할 수 있으니, 반드시 재학습 시 동일한 모델이 나오는지 확인하시기 바랍니다.

```python
# pytorch 시드 고정
import torch
import numpy as np
import random

random_seed = 42
torch.manual_seed(random_seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
np.random.seed(random_seed)
random.seed(random_seed)
torch.cuda.manual_seed(random_seed)
```

```python
# tensorflow 시드 고정
import os
import tensorflow as tf
import numpy as np
import random

SEED = 42
os.environ['PYTHONHASHSEED'] = str(SEED)
os.environ['TF_DETERMINISTIC_OPS'] = '1'
tf.random.set_seed(SEED)
np.random.seed(SEED)
random.seed(SEED)
```

## 5. 추론 결과 제출

* submit.py  내 submit 함수로 추론결과를 제출하고, 리더보드 상에서 결과를 확인할 수 있습니다.
* 입력인자
  * task_no:  테스크 번호(1: 치아, 2: 구강암)
  * user_id: 사용자 아이디
  * pwd: 사용자 비밀번호
  * modelnm:  제출파일 식별 문자
    * 참가자가 본인이 제출한 파일을 식별할 수 있도록 자유롭게 작성 가능
    * `제출이력`에서 확인 가능
  * result: 제출파일 경로
* 실행

```bash
python submit.py --task_no 1 --user_id test_user --pwd 1234 --modelnm first --result ./sample_submission.csv
```

