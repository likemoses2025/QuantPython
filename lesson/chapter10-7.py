import pymysql
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

#! 전종목 가치지표 계산

# 패키지 불러오기


# DB 연결
engine = create_engine("mysql+pymysql://root:!!akswhr23@127.0.0.1:3306/stock_db")
con = pymysql.connect(
    user="root", passwd="!!akswhr23", host="127.0.0.1", db="stock_db", charset="utf8"
)
mycursor = con.cursor()

# 분기 재무제표 불러오기
kor_fs = pd.read_sql(
    """
select * from kor_fs
where 공시구분 = 'q'
and 계정 in ('당기순이익', '자본', '영업활동으로인한현금흐름', '매출액');
""",
    con=engine,
)

# 티커 리스트 불러오기
ticker_list = pd.read_sql(
    """
select * from kor_ticker
where 기준일 = (select max(기준일) from kor_ticker) 
and 종목구분 = '보통주';
""",
    con=engine,
)

# TTM 구하기 (4분기 합계)
kor_fs = kor_fs.sort_values(["종목코드", "계정", "기준일"])
kor_fs["ttm"] = (
    kor_fs.groupby(["종목코드", "계정"], as_index=False)["값"]
    .rolling(window=4, min_periods=4)
    .sum()["값"]
)

# TTM 자본은 평균(/4) 구하기
kor_fs["ttm"] = np.where(kor_fs["계정"] == "자본", kor_fs["ttm"] / 4, kor_fs["ttm"])
kor_fs = kor_fs.groupby(["계정", "종목코드"]).tail(1)

# 가치지표 계산
kor_fs_merge = kor_fs[["계정", "종목코드", "ttm"]].merge(
    ticker_list[["종목코드", "시가총액", "기준일"]], on="종목코드"
)
kor_fs_merge["시가총액"] = kor_fs_merge["시가총액"] / 100000000

kor_fs_merge["value"] = kor_fs_merge["시가총액"] / kor_fs_merge["ttm"]
# 반올림
kor_fs_merge["value"] = kor_fs_merge["value"].round(4)
kor_fs_merge["지표"] = np.where(
    kor_fs_merge["계정"] == "매출액",
    "PSR",
    np.where(
        kor_fs_merge["계정"] == "영업활동으로인한현금흐름",
        "PCR",
        np.where(
            kor_fs_merge["계정"] == "자본",
            "PBR",
            np.where(kor_fs_merge["계정"] == "당기순이익", "PER", None),  # type: ignore
        ),
    ),
)

kor_fs_merge.rename(columns={"value": "값"}, inplace=True)
kor_fs_merge = kor_fs_merge[["종목코드", "기준일", "지표", "값"]]
kor_fs_merge = kor_fs_merge.replace([np.inf, -np.inf, np.nan], None)

kor_fs_merge.head(4)
# 종목코드	기준일	지표	값
# 0	000020	2022-08-03	PER	14.9532
# 1	000020	2022-08-03	PSR	0.9660
# 2	000020	2022-08-03	PCR	6.7597
# 3	000020	2022-08-03	PBR	0.8314

# ? 계산된 가치지표를 데이터베이스에 저장
query = """
    insert into kor_value (종목코드, 기준일, 지표, 값)
    values (%s,%s,%s,%s) as new
    on duplicate key update
    값=new.값
"""

args_fs = kor_fs_merge.values.tolist()
mycursor.executemany(query, args_fs)
con.commit()

# ? 배당수익율의 계산
ticker_list["값"] = ticker_list["주당배당금"] / ticker_list["종가"]
ticker_list["값"] = ticker_list["값"].round(4)  # 반올림
ticker_list["지표"] = "DY"
dy_list = ticker_list[["종목코드", "기준일", "지표", "값"]]
# inf, nan을 None으로 변환
dy_list = dy_list.replace([np.inf, -np.inf, np.nan], None)
# 배당금이 0인 값 제외
dy_list = dy_list[dy_list["값"] != 0]

print(dy_list.head())
# 종목코드	기준일	지표	값
# 0  000020  2023-11-24  DY  0.0186
# 2  000050  2023-11-24  DY  0.0147
# 3  000070  2023-11-24  DY  0.0509
# 4  000080  2023-11-24  DY  0.0416
# 5  000100  2023-11-24  DY  0.0065

args_dy = dy_list.values.tolist()
mycursor.executemany(query, args_dy)
con.commit()
con.close()
