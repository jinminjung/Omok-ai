import os
from glob import glob
from tqdm import tqdm

# Dataset 정보
game_rule = 'Freestyle1'
base_path = r"C:\Users\JINMIN\Downloads\gomocup2023results\Freestyle1"
output_path = os.path.join('dataset', os.path.basename(base_path))

# 디렉토리 생성
os.makedirs(output_path, exist_ok=True)

# 경로가 제대로 설정되었는지 확인
print(f"Base path: {base_path}")
print(f"Output path: {output_path}")

# 파일 경로 패턴 확인
file_list = glob(os.path.join(base_path, f'{game_rule}*', '*.psq'))

# 파일이 있는지 출력하여 확인
print(f"찾은 파일 목록: {file_list}")
if not file_list:
    print("지정된 경로에 파일이 없습니다. 경로와 패턴을 다시 확인하세요.")
else:
    print(f"총 {len(file_list)}개의 파일이 발견되었습니다.")

# 진행 표시줄 사용
for index, file_path in enumerate(tqdm(file_list)):
    # 파일 처리 로직...
    pass
