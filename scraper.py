import json
from datetime import datetime

# 1. 시세 데이터 세팅
today_date = datetime.now().strftime("%Y.%m.%d 기준 (자동 업데이트)")

market_data = [
    {
        "name": "동래 래미안 아이파크 (84㎡)",
        "initial_price": "14.9억",
        "current_price": "19.5억",
        "premium": "+4.6억",
        "percent": "30.8",
        "updated_at": today_date
    },
    {
        "name": "동래 롯데캐슬 퀸 (84㎡)",
        "initial_price": "12.2억",
        "current_price": "15.8억",
        "premium": "+3.6억",
        "percent": "29.5",
        "updated_at": today_date
    },
    {
        "name": "동래 더샵 (84㎡)",
        "initial_price": "11.5억",
        "current_price": "14.2억",
        "premium": "+2.7억",
        "percent": "23.4",
        "updated_at": today_date
    }
]

# 2. JSON 파일로 저장 (깃허브 폴더 안에 바로 저장됨)
filename = "market_data.json"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(market_data, f, ensure_ascii=False, indent=4)

print(f"[{today_date}] JSON 파일 깃허브 저장 완료.")
