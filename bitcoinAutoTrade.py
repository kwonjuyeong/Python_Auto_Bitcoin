import time
import pyupbit
import datetime

access = "Nia4PY7Y6rigKBV9xE0fHFKfumPmTsXuqDHYPT2M"
secret = "660awV9GFlJBQPFUY4hj9wdxgaNwVVUxNxNdx9qx"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price #변동성을 파악하여 조건과 맞으면 return해준다.

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC") #시작시간 9:00로 설정
        end_time = start_time + datetime.timedelta(days=1) #9:00 + 1일 마감시간
		# 9:00 < 현재가 < 8:59:50
        if start_time < now < end_time - datetime.timedelta(seconds=10): #9시부터 9시까지 설정에서 10초를 빼줌으로써 8시59분50초까지 돌아가게 한다.
            target_price = get_target_price("KRW-BTC", 0.5)#target_price를 직접 구해도 됨. k값도 직접 설정할 수 있음.
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_balance("KRW") #원화 잔고 조회
                if krw > 5000: #원화 잔고가 최소 거래 금액 5000원보다 많으면
                    upbit.buy_market_order("KRW-BTC", krw*0.9995) #코인을 매수
        else:
        	#9시부터 8시59분50초 사이 10초에 비트코인 전량 매도.
            btc = get_balance("BTC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*0.9995) #수수료 0.05를 고려
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)