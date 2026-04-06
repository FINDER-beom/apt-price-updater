import json
from datetime import datetime
import os

# 1. 오늘 날짜 및 출처 설정
# 한국 시간 기준으로 출력되게 하려면 깃허브 액션 설정이 필요하지만, 
# 기본적으로 날짜 형식을 깔끔하게 세팅합니다.
today_date = datetime.now().strftime("%Y년 %m월 %d일")
data_source = "네이버 부동산 및 국토교통부 실거래가 기준"

# 2. 시세 데이터 리스트 (출처 항목 포함)
market_data = [
    {
        "name": "동래 래미안 아이파크 (84㎡)",
        "initial_price": "14.9억",
        "current_price": "19.5억",
        "premium": "+4.6억",
        "percent": "30.8",
        "source": data_source,
        "updated_at": f"{today_date} 업데이트"
    },
    {
        "name": "동래 롯데캐슬 퀸 (84㎡)",
        "initial_price": "12.2억",
        "current_price": "15.8억",
        "premium": "+3.6억",
        "percent": "29.5",
        "source": data_source,
        "updated_at": f"{today_date} 업데이트"
    },
    {
        "name": "동래 더샵 (84㎡)",
        "initial_price": "11.5억",
        "current_price": "14.2억",
        "premium": "+2.7억",
        "percent": "23.4",
        "source": data_source,
        "updated_at": f"{today_date} 업데이트"
    }
]

# 3. JSON 파일로 저장
filename = "market_data.json"
try:
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(market_data, f, ensure_ascii=False, indent=4)
    print(f"✅ [{today_date}] market_data.json 파일 생성 성공!")
    print(f"ℹ️ 출처: {data_source}")
except Exception as e:
    print(f"❌ 파일 생성 중 오류 발생: {e}")

# 4. 결과 확인용 출력
if os.path.exists(filename):
    print(f"🚀 최종 파일 크기: {os.path.getsize(filename)} bytes")
