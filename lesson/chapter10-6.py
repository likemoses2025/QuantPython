from sqlalchemy import create_engine
import pandas as pd


# ! 가치지표 계산

# *| 지표 | 설명                     | 필요한 재무제표 데이터 |
# *| PER | Price to Earnings Ratio | Earnings (순이익) |
# *| PBR | Price to Book Ratio | Book Value (순자산) |
# *| PCR | Price to Cash Flow Ratio | Cash Flow (영업활동현금흐름) |
# *| PSR | Price to Sales Ratio | Sales (매출액) |
# *| DY | Dividend Yield | Dividened (배당) |

# @  TTM - Trading twelve Months ( 4분기 데이터 이용)

engine = create_engine("mysql+pymysql://root:!!akswhr23@127.0.0.1:3306/stock_db")

ticker_list = pd.read_sql(
    """select * from kor_ticker where 기준일 = (select max(기준일) from kor_ticker) and 종목구분="보통주"; """,
    con=engine,
)

# ? 삼성전자 분기 재무제표
sample_fs = pd.read_sql(
    """select * from kor_fs where 공시구분 = "q" and 종목코드="005930" and 계정 in("당기순이익","자본","영업활동으로인한현금흐름","매출액"); """,
    con=engine,
)

sample_fs = sample_fs.sort_values(["종목코드", "계정", "기준일"])
print(sample_fs.head())
# 	계정	기준일	값	종목코드	공시구분
# 0	당기순이익	2021-06-30	96345.0	005930	q
# 1	당기순이익	2021-09-30	122933.0	005930	q
# 2	당기순이익	2021-12-31	108379.0	005930	q
# 3	당기순이익	2022-03-31	113246.0	005930	q
# 4	매출액	2021-06-30	636716.0	005930	q


# @ sort_values() 함수를 통해 재무제표 데이터를 종목코드, 계정, 기준일 순으로 정렬
# 종목코드와 계정을 기준으로 groupby() 함수를 통해 그룹을 묶으며, as_index=False를 통해 그룹 라벨을 인덱스로 사용하지 않는다.
# rolling() 메서드를 통해 4개 기간씩 합계를 구하며, min_periods 인자를 통해 데이터가 최소 4개는 있을 경우에만 값을 구한다.
# 즉 4개 분기 데이터를 통해 TTM 값을 계산하며, 12개월치 데이터가 없을 경우는 계산을 하지 않는다.
sample_fs["ttm"] = (
    sample_fs.groupby(["종목코드", "계정"], as_index=False)["값"]
    .rolling(window=4, min_periods=4)
    .sum()["값"]
)

print("SAMPLE FS", sample_fs)
# 	계정	기준일	값	종목코드	공시구분	ttm
# 0	당기순이익	2021-06-30	96345.0	005930	q	NaN
# 1	당기순이익	2021-09-30	122933.0	005930	q	NaN
# 2	당기순이익	2021-12-31	108379.0	005930	q	NaN
# 3	당기순이익	2022-03-31	113246.0	005930	q	440903.0
# 4	매출액	2021-06-30	636716.0	005930	q	NaN
# 5	매출액	2021-09-30	739792.0	005930	q	NaN
# 6	매출액	2021-12-31	765655.0	005930	q	NaN
# 7	매출액	2022-03-31	777815.0	005930	q	2919978.0
# 8	영업활동으로인한현금흐름	2021-06-30	120865.0	005930	q	NaN
# 9	영업활동으로인한현금흐름	2021-09-30	185815.0	005930	q	NaN
# 10	영업활동으로인한현금흐름	2021-12-31	206345.0	005930	q	NaN
# 11	영업활동으로인한현금흐름	2022-03-31	104531.0	005930	q	617556.0
# 12	자본	2021-06-30	2823240.0	005930	q	NaN
# 13	자본	2021-09-30	2967660.0	005930	q	NaN
# 14	자본	2021-12-31	3049000.0	005930	q	NaN
# 15	자본	2022-03-31	3152910.0	005930	q	11992810.0

import numpy as np

# '자본' 항목은 재무상태표에 해당하는 항목이므로 합이 아닌 4로 나누어 평균을 구하며, 타 헝목은 4분기 기준 합을 그대로 사용한다.
# 계정과 종목코드별 그룹을 나누 후 tail(1) 함수를 통해 가장 최근 데이터만 선택한다.

sample_fs["ttm"] = np.where(
    sample_fs["계정"] == "자본", sample_fs["ttm"] / 4, sample_fs["ttm"]
)
sample_fs = sample_fs.groupby(["계정", "종목코드"]).tail(1)

print(sample_fs.head())
# 	계정	기준일	값	종목코드	공시구분	ttm
# 3	당기순이익	2022-03-31	113246.0	005930	q	440903.0
# 7	매출액	2022-03-31	777815.0	005930	q	2919978.0
# 11	영업활동으로인한현금흐름	2022-03-31	104531.0	005930	q	617556.0
# 15	자본	2022-03-31	3152910.0	005930	q	2998202.5

# @ 시가총액 구하기

sample_fs_merge = sample_fs[["계정", "종목코드", "ttm"]].merge(
    ticker_list[["종목코드", "시가총액", "기준일"]], on="종목코드"
)
sample_fs_merge["시가총액"] = sample_fs_merge["시가총액"] / 100000000

sample_fs_merge.head()
# 계정	종목코드	ttm	시가총액	기준일
# 0	당기순이익	005930	440903.0	3659480.0	2022-08-03
# 1	매출액	005930	2919978.0	3659480.0	2022-08-03
# 2	영업활동으로인한현금흐름	005930	617556.0	3659480.0	2022-08-03
# 3	자본	005930	2998202.5	3659480.0	2022-08-03

sample_fs_merge["value"] = sample_fs_merge["시가총액"] / sample_fs_merge["ttm"]
sample_fs_merge["지표"] = np.where(
    sample_fs_merge["계정"] == "매출액",
    "PSR",
    np.where(
        sample_fs_merge["계정"] == "영업활동으로인한현금흐름",
        "PCR",
        np.where(
            sample_fs_merge["계정"] == "자본",
            "PBR",
            np.where(sample_fs_merge["계정"] == "당기순이익", "PER", None),  # type: ignore
        ),
    ),
)

print(sample_fs_merge)
# 계정	종목코드	ttm	시가총액	기준일	value	지표
# 0	당기순이익	005930	440903.0	3659480.0	2022-08-03	8.299966	PER
# 1	매출액	005930	2919978.0	3659480.0	2022-08-03	1.253256	PSR
# 2	영업활동으로인한현금흐름	005930	617556.0	3659480.0	2022-08-03	5.925746	PCR
# 3	자본	005930	2998202.5	3659480.0	2022-08-03	1.220558	PBR

# @ 배당수익율 계산 - 주당배당금 / 종가
ticker_list_sample = ticker_list[ticker_list["종목코드"] == "005930"].copy()
ticker_list_sample["DY"] = ticker_list_sample["주당배당금"] / ticker_list_sample["종가"]
ticker_list_sample.head()
# 	종목코드	종목명	시장구분	종가	시가총액	기준일	EPS	선행EPS	BPS	주당배당금	종목구분	DY
# 260	005930	삼성전자	KOSPI	61300.0	3.659480e+14	2022-08-03	5777.0	5900.0	43611.0	1444.0	보통주	0.023556
