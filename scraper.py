import json
import ftplib
import os
from datetime import datetime

# 1. 시세 데이터 세팅 (실제 크롤링(BeautifulSoup 등) 코드를 추후 이 부분에 넣습니다)
# 매일 자동으로 오늘 날짜가 갱신되어 홈페이지에 표시됩니다.
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

# 2. JSON 파일로 저장
filename = "market_data.json"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(market_data, f, ensure_ascii=False, indent=4)

print(f"[{today_date}] JSON 파일 생성 완료.")

# 3. 깃허브 서버에서 닷홈 FTP로 자동 업로드
FTP_HOST = os.environ.get("FTP_HOST")
FTP_USER = os.environ.get("FTP_USER")
FTP_PASS = os.environ.get("FTP_PASS")
# 닷홈은 보통 기본 파일 경로가 /html 입니다. json 파일을 넣을 경로를 지정합니다.
FTP_DIR = os.environ.get("FTP_DIR", "/html") 

if FTP_HOST and FTP_USER and FTP_PASS:
    try:
        # FTP 서버 접속
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd(FTP_DIR)
        
        # 파일 덮어쓰기 (업로드)
        with open(filename, 'rb') as f:
            ftp.storbinary(f'STOR {filename}', f)
            
        ftp.quit()
        print("🚀 닷홈 서버 FTP 업로드 완벽 성공!")
    except Exception as e:
        print(f"❌ FTP 업로드 실패: {e}")
else:
    print("⚠️ 깃허브 시크릿(FTP 정보)이 설정되지 않아 파일이 전송되지 않았습니다.")
